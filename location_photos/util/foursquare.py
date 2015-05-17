# FourSquare Venue Photos

import apiconfig
import requests

if __name__ == "__main__":
	print 'Module for FourSquare Venues photo search.'
	print 'Usage: search(venue_id="<id>", **kwargs)'
	print 'Available arguments (with their default values): '
	print """
VENUE_ID	XXX123YYYY	required The venue you want photos for.

group	checkin		If not specified, public venue photos are returned ordered by relevance. 
					Pass venue for public venue photos, ordered by recency.
					Pass checkin for venue photos from friends (including non-public photos from recent checkins), ordered by recency. 

limit	100			Number of results to return, up to 200.

offset	100			Used to page through results.
"""

def search(id=None, **kwargs):

	if not id:
		raise Exception('Venue id is needed for search!')

	kwargs['client_id'] 	= apiconfig.FOURSQUARE_APP_CLIENT_ID
	kwargs['client_secret']	= apiconfig.FOURSQUARE_APP_CLIENT_SECRET
	kwargs['v']				= apiconfig.FOURSQUARE_API_VERSION_DATE
	kwargs['m']				= apiconfig.FOURSQUARE_API_RESPONSE_STYLE
	
	url 		= "https://api.foursquare.com/v2/venues/%s/photos" % id
	response 	= requests.get(url, params=kwargs)
	return response.json()
