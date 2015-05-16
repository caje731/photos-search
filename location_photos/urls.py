from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^locations/(?P<location_id>[0-9]+)/photos/(?P<photo_id>[0-9]*)', views.photos, name='locations_photos:photos'),
	url(r'^search/photos', views.photos_search, name='locations_photos:photos_search')
]