from tastypie.resources import ModelResource
from api.models import Weather

class WeatherResource(ModelResource):
    class Meta:
        queryset = Weather.objects.all() #da erro mas esta a correr?
        resource_name = 'weather'
		#authorization = Authorization() #para autorizar no entanto esta a funcionar sem isto?

		