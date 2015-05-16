from django.contrib import admin

# Register your models here.
from location_photos.models import Location, Photo

# Customising the admin site look
admin.site.site_header 	= 	"Location Repository Administration"
admin.site.site_title 	=	"Location repo admin"
admin.site.site_url		=	None
admin.site.index_title	=	"Manage your locations"

# Action button handler for deleting all photos of a location
def delete_photos_for_location(modeladmin, request, queryset):
	for location in queryset:
		location.photos.all().delete()
delete_photos_for_location.short_description = "Delete photos of selected locations"

class LocationAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'city', 'country', 'loc_type', 'lat', 'lng', 'facebook_id', 'foursquare_id', 'created_at')
	actions = [delete_photos_for_location]
		
admin.site.register(Location, LocationAdmin)
admin.site.register(Photo)

