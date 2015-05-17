# Google Custom Search

import apiconfig
import requests

if __name__ == '__main__':
	print 'Module for Google Custom Search.'
	print 'Usage: search(q="query", **kwargs)'
	print 'Available arguments: '
	print """
q 				:	Query (string)
c2coff 			:	Turns off the translation between zh-CN and zh-TW. (string)
cr 				: 	Country restrict(s). (string)
cref			:	The URL of a linked custom search engine (string)
cx				:	The custom search engine ID to scope this search query (string)
dateRestrict	:	Specifies all search results are from a time period (string)
exactTerms		:	Identifies a phrase that all documents in the search results must contain (string)
excludeTerms	:	Identifies a word or phrase that should not appear in any documents in the search results (string)
fileType		:	Returns images of a specified type. Some of the allowed values are: bmp, gif, png, jpg, svg, pdf, ... (string)
filter			:	Controls turning on or off the duplicate content filter. (string)
gl				:	Geolocation of end user. (string)
googlehost		:	The local Google domain to use to perform the search. (string)
highRange		:	Creates a range in form as_nlo value..as_nhi value and attempts to append it to query (string)
hl				:	Sets the user interface language. (string)
hq				:	Appends the extra query terms to the query. (string)
imgColorType	:	Returns black and white, grayscale, or color images: mono, gray, and color. (string)
imgDominantColor:	Returns images of a specific dominant color: yellow, green, teal, blue, purple, pink, white, gray, black and brown. (string)
imgSize			:	Returns images of a specified size, where size can be one of: icon, small, medium, large, xlarge, xxlarge, and huge. (string)
imgType			:	Returns images of a type, which can be one of: clipart, face, lineart, news, and photo. (string)
linkSite		:	Specifies that all search results should contain a link to a particular URL (string)
lowRange		:	Creates a range in form as_nlo value..as_nhi value and attempts to append it to query (string)
lr				:	The language restriction for the search results (string)
num				:	Number of search results to return (integer)
orTerms			:	Provides additional search terms to check for in a document, where each document in the search results must contain at least one of the additional search terms (string)
relatedSite		:	Specifies that all search results should be pages that are related to the specified URL (string)
rights			:	Filters based on licensing. Supported values include: cc_publicdomain, cc_attribute, cc_sharealike, cc_noncommercial, cc_nonderived and combinations of these. (string)
safe			:	Search safety level (string)
searchType		:	Specifies the search type: image. (string)
siteSearch		:	Specifies all search results should be pages from a given site (string)
siteSearchFilter:	Controls whether to include or exclude results from the site named in the as_sitesearch parameter (string)
sort			:	The sort expression to apply to the results (string)
start			:	The index of the first result to return (integer)
fields			:	Selector specifying which fields to include in a partial response.
"""
	pass

def search(q=None, **kwargs):
	
	if not q:
		raise Exception('Query parameter q is mandatory!')

	kwargs['q'] 	= q
	kwargs['key'] 	= apiconfig.GOOGLE_API_KEY
	kwargs['cx']	= apiconfig.GOOGLE_CSE_ID
	kwargs['searchType']= 'image'
	kwargs['imgSize'] 	= 'xxlarge'
	kwargs['rights'] 	= 'cc_attribute'

	url 		= "https://www.googleapis.com/customsearch/v1?key=" + apiconfig.GOOGLE_API_KEY
	response 	= requests.get(url, params=kwargs)
	return response.json()
	