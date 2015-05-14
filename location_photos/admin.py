from django.contrib import admin

# Register your models here.
from location_photos.models import Location, Photo

# Customising the admin site look
admin.site.site_header 	= 	"Location Repository Administration"
admin.site.site_title 	=	"Location repo admin"
admin.site.site_url		=	None
admin.site.index_title	=	"Manage your locations"


class LocationAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'city', 'country', 'loc_type', 'lat', 'lng', 'facebook_id', 'foursquare_id', 'created_at')
		
admin.site.register(Location, LocationAdmin)
admin.site.register(Photo)

