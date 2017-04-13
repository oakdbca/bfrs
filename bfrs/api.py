from django.conf.urls import url
from tastypie.resources import ModelResource, Resource
from tastypie.authorization import Authorization, ReadOnlyAuthorization, DjangoAuthorization
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.api import Api
from tastypie import fields
from bfrs.models import Profile, Region, District, Bushfire, Tenure
from bfrs.utils import update_areas_burnt, invalidate_bushfire
from django.contrib.auth.models import User
from django.contrib.gis.geos import Point, GEOSGeometry, Polygon, MultiPolygon, GEOSException
from tastypie.http import HttpBadRequest
from tastypie.exceptions import ImmediateHttpResponse

"""
The two helper methods below allow to replace class like:

class BushfireResource(ModelResource):
    class Meta:
        queryset = Bushfire.objects.all()
        resource_name = 'bushfire'
        filtering = {
            'regions': ALL_WITH_RELATIONS,
            'incident_no': ALL_WITH_RELATIONS,
            'name': ALL_WITH_RELATIONS,
        }
        authorization= Authorization()

with:

class BushfireResource(ModelResource):
    Meta = generate_meta(Bushfire)

"""

def generate_filtering(mdl):
    """Utility function to add all model fields to filtering whitelist.
    See: http://django-tastypie.readthedocs.org/en/latest/resources.html#basic-filtering
    """
    filtering = {}
    for field in mdl._meta.fields:
        filtering.update({field.name: ALL_WITH_RELATIONS})
    return filtering


def generate_meta(klass):
    return type('Meta', (object,), {
        'queryset': klass.objects.all(),
        'resource_name': klass._meta.model_name,
        'filtering': generate_filtering(klass),
        'authorization': Authorization(),
        'always_return_data': True
    })


class APIResource(ModelResource):
    class Meta:
        pass

    def prepend_urls(self):
        return [
            url(
                r"^(?P<resource_name>{})/fields/(?P<field_name>[\w\d_.-]+)/$".format(self._meta.resource_name),
                self.wrap_view('field_values'), name="api_field_values"),
        ]

    def field_values(self, request, **kwargs):
        # Get a list of unique values for the field passed in kwargs.
        try:
            qs = self._meta.queryset.values_list(kwargs['field_name'], flat=True).distinct()
        except FieldError as e:
            return self.create_response(request, data={'error': str(e)}, response_class=HttpBadRequest)
        # Prepare return the HttpResponse.
        return self.create_response(request, data=list(qs))


class ProfileResource(APIResource):
    class Meta:
        queryset = Profile.objects.all()
        resource_name = 'profile'
        authorization= ReadOnlyAuthorization()

    def prepend_urls(self):
        return [
            url(
                r"^(?P<resource_name>{})/$".format(self._meta.resource_name),
                self.wrap_view('field_values'), name="api_field_values"),
        ]

    def field_values(self, request, **kwargs):
        try:
            qs = self._meta.queryset.filter(id=request.user.profile.id)
            data = qs[0].to_dict() if len(qs)>0 else None
        except FieldError as e:
            return self.create_response(request, data={'error': str(e)}, response_class=HttpBadRequest)
        return self.create_response(request, data=data)

class RegionResource(APIResource):
    class Meta:
        queryset = Region.objects.all()
        resource_name = 'region'
        authorization= ReadOnlyAuthorization()

    def prepend_urls(self):
        return [
            url(
                r"^(?P<resource_name>{})/$".format(self._meta.resource_name),
                self.wrap_view('field_values'), name="api_field_values"),
        ]

    def field_values(self, request, **kwargs):
        try:
            qs = Region.objects.all().distinct()
        except FieldError as e:
            return self.create_response(request, data={'error': str(e)}, response_class=HttpBadRequest)
        return self.create_response(request, data=([q.to_dict() for q in qs]))

class TenureResource(APIResource):
    class Meta:
        queryset = Tenure.objects.all()
        resource_name = 'tenure'
        authorization= Authorization()
        #fields = ['origin_point', 'fire_boundary', 'area', 'fire_position', 'tenure_id']


class BushfireResource(APIResource):
    """ http://localhost:8000/api/v1/bushfire/?format=json
        curl --dump-header - -H "Content-Type: application/json" -X PATCH --data '{"origin_point":[11,-12], "area":12347, "fire_boundary": [[[[115.6528663436689,-31.177579372720448],[116.20507608972612,-31.386375097597803],[116.36167288338414,-31.009993330384674],[115.77374807912422,-30.999004081706918],[115.6528663436689,-31.177579372720448]]]]}' http://localhost:8000/api/v1/bushfire/1/?format=json
    """

    tenure = fields.ToOneField(TenureResource, 'tenure')

    class Meta:
        queryset = Bushfire.objects.all()
        resource_name = 'bushfire'
        authorization= Authorization()
        #fields = ['origin_point', 'fire_boundary', 'area', 'fire_position']
        fields = ['origin_point', 'fire_boundary']

    def hydrate_origin_point(self, bundle):
        """
        Converts the json string format to the one required by tastypie's full_hydrate() method
        converts the string: [11,-12] --> POINT (11 -12)
        """
        if bundle.data.has_key('origin_point') and isinstance(bundle.data['origin_point'], list):
            bundle.data['origin_point'] = Point(bundle.data['origin_point']).__str__()
        return bundle

    def hydrate_fire_boundary(self, bundle):
        #import ipdb; ipdb.set_trace()
        if bundle.data.has_key('fire_boundary') and isinstance(bundle.data['fire_boundary'], list):
            bundle.data['fire_boundary'] = MultiPolygon([Polygon(p[0]) for p in bundle.data['fire_boundary']]).__str__()
        return bundle

    def obj_update(self, bundle, **kwargs):
        #import ipdb; ipdb.set_trace()
        self.full_hydrate(bundle)
        if bundle.data.has_key('tenure_ignition_point') and bundle.data['tenure_ignition_point'] and \
            bundle.data['tenure_ignition_point'].has_key('category') and bundle.data['tenure_ignition_point']['category']:
            try:
                bundle.obj.tenure = Tenure.objects.get(name__istartswith=bundle.data['tenure_ignition_point']['category'])
            except:
                bundle.obj.tenure = Tenure.objects.get(name__istartswith='other')
        else:
            bundle.obj.tenure = Tenure.objects.get(name__istartswith='other')

        if bundle.data.has_key('tenure_area') and bundle.data['tenure_area']:
            update_areas_burnt(bundle.obj, bundle.data['tenure_area'])

        if bundle.data.has_key('area') and bundle.data['area']:
            if float(bundle.data['area']) > 2.0:
                bundle.obj.area_limit = False
                bundle.obj.area = float(bundle.data['area'])

        if bundle.data.has_key('fire_position') and bundle.data['fire_position']:
            # only update if user has not over-ridden
            if not bundle.obj.fire_position_override:
                bundle.obj.fire_position = bundle.data['fire_position']

        if bundle.data.has_key('region_id') and bundle.data.has_key('district_id') and bundle.data['region_id'] and bundle.data['district_id']:
            if bundle.data['district_id'] != bundle.obj.district.id and bundle.obj.report_status == Bushfire.STATUS_INITIAL:
                district = District.objects.get(id=bundle.data['district_id'])
                invalidate_bushfire(bundle.obj, district, bundle.request.user)
                #bundle.obj.district = district
                #bundle.obj.region = district.region

        bundle.obj.save()
        return bundle




v1_api = Api(api_name='v1')
v1_api.register(BushfireResource())
v1_api.register(ProfileResource())
v1_api.register(RegionResource())
v1_api.register(TenureResource())
