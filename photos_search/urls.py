from django.conf.urls import include, url
from django.contrib import admin
import location_photos

urlpatterns = [
    # Examples:
    # url(r'^$', 'photos_search.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^location_photos/', include('location_photos.urls')),
]
