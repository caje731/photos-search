from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse
from location_photos.models import Location, Photo

# Create your views here.
GET 	= "GET"
POST	= "POST"
PUT		= "PUT"
DELETE 	= "DELETE"

def photos(request, location_id):
	if(request.method==GET):
		return get_photos(request, location_id)

	elif(request.method==POST):
		return post_photos(request, location_id)

def get_photos(request, location_id):
	loc_photos = Location.objects.get(pk=location_id).photos.all()
	if loc_photos:
		return JsonResponse(serializers.serialize('json', loc_photos),safe=False)
	else:
		return JsonResponse({'data':[] })

def post_photos(request):
	print "Fetching new photos"
	return