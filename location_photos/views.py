from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse, StreamingHttpResponse
from location_photos.models import Location, Photo
import time

# Create your views here.
GET 	= "GET"
POST	= "POST"
PUT		= "PUT"
DELETE 	= "DELETE"

def photos(request, location_id, photo_id):
	if(request.method==GET):
		return get_photos(request, location_id)

	elif(request.method==DELETE):
		return delete_photo(request, location_id, photo_id)

def get_photos(request, location_id):
	loc = Location.objects.get(pk=location_id)
	loc_photos = loc.photos.all()
	if loc_photos:
		return JsonResponse(serializers.serialize('json', loc_photos),safe=False)
	else:
		return JsonResponse({'error' : 'No photos found for '+loc.name })

def delete_photo(request, location_id, photo_id=None):
	if photo_id:
		try:
			Photo.objects.get(pk=photo_id).delete()
			return JsonResponse({'status' : 'ok', 'code' : 200, 'msg': 'success' }, status=200)
		
		except Exception, e:
			return JsonResponse({'status' : 'error', 'code' : 500, 'msg': 'failed' }, status=500)
			

def stream_response(request):
    return StreamingHttpResponse(stream_response_generator())

def stream_response_generator():
    for x in range(1,11):
        yield "|<p>%s<p>\n" % x
        yield " " * 1024  # Encourage browser to render incrementally
        time.sleep(1)
    

def photos_search(request):
	return stream_response(request)