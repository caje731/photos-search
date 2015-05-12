from django.contrib import admin

# Register your models here.
from location_photos.models import Location, Photo

admin.site.register(Location)
admin.site.register(Photo)