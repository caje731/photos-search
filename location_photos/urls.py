from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^locations/(?P<location_id>[0-9]+)/photos', views.photos, name='locations_photos:photos')
]