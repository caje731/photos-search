from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse, StreamingHttpResponse
from django.db.models import Count

from location_photos.models import Location, Photo
from util import gcs, foursquare, apiconfig

import time, json

# Create your views here.
GET 	= "GET"
POST	= "POST"
PUT		= "PUT"
DELETE 	= "DELETE"

# ============================ View functions ===================================

def photos(request, location_id, photo_id):
	if(request.method==GET):
		return get_photos(request, location_id)

	elif(request.method==DELETE):
		return delete_photo(request, location_id, photo_id)

""" AJAX handler for triggering a photo search """
def photos_search(request):
	return stream_response(request)

# =========================== End View functions =================================




#============================ Helpers ============================================

""" AJAX handler for fetching all photos of a particular location """
def get_photos(request, location_id):
	loc = Location.objects.get(pk=location_id)
	loc_photos = loc.photos.all()
	if loc_photos:
		return JsonResponse(serializers.serialize('json', loc_photos),safe=False)
	else:
		return JsonResponse({'error' : 'No photos found for '+loc.name })


""" AJAX handler for deleting a particular photo """
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
    locations = Location.objects.annotate(photo_count=Count('photo')).filter(photo_count=0)
    if not locations:
    	yield "|<p class='text-danger'>Either no locations added, or all locations already have photos!</p>\n"
    	yield " " * 1024
    	return

    for location in locations:
    	full_name 	= location.name + ' ' + location.city + ' ' + location.country
    	added_count = 0
    	failed_count= 0

    	print location.loc_type
    	# Search venue images on foursquare
    	if location.loc_type ==1:
    		limit = 10 			# For restaurants/pubs, depend solely on foursquare (for the quota of 10 images)
    	else:
    		limit = 5 			# For all other types, mix results from foursquare and google

    	response = foursquare.search(id = location.foursquare_id, limit=limit)
    	if response['response']['photos']['count'] > 0:
    		for item in response['response']['photos']['items']:
    			height 	= item['height']
    			width	= item['width']
    			link 	= item['prefix'] + 'original'+item['suffix']
    			attrib  = "https://foursquare.com/v/%s?ref=%s" % (location.foursquare_id, apiconfig.FOURSQUARE_APP_CLIENT_ID)
    			title   = '' # I'm undecided on what title to use, for photos from foursquare

    			if height>=600 or width>=600:
    				photo   =  Photo(link=link, attribution=attrib, title=title, location=location, height=height, width=width)
	    			try:
	    				photo.save()
	    				added_count +=1

	    			except IntegrityException, e:
	    				failed_count+=1

    	# If location is not a restaurant/pub, search images on Google also
    	if location.loc_type != 1:
	    	response 	= gcs.search(q=full_name, num=(10-added_count))
	    	if 'items' in response:
		    	for item in response['items']:
		    		link 	= 	item['link']
		    		title 	=  	item['title']
		    		dplink	=	item['displayLink']
		    		height	=	item['image']['height']
		    		width	=	item['image']['width']
		    		size 	= 	item['image']['byteSize']

		    		photo   =  Photo(link=link, attribution=dplink, title=title, location=location, height=height, width=width, bytes=size)
		    		try:
		    			photo.save()
		    			added_count +=1

		    		except IntegrityException, e:
		    			failed_count+=1
			else:
				print 'Google search failed for '+location.name
				print response

    	yield "|<p>ID:%s %s \n" % (location.id, location.name)
    	yield "<span class='text-success'>Added :%s</span> <span class='text-warning'>Failed :%s</span></p>\n" % (added_count, failed_count)
    	yield " "  * 1024 # Encourage browser to render incrementally


    	

#=========================== End Helpers ===========================================