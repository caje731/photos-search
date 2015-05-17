from django.db import models

# Create your models here.

# =====================================================================================================

class Location(models.Model):

	LOCATION_TYPE_CHOICES = [
								(1, 'Restaurant / Eatery'),
								(2, 'Monument / Tourist Place')
							]

	# Details of the point of interest
	name 	= models.CharField(blank=False, max_length=100)	# Gateway Of India
	city 	= models.CharField(blank=True, max_length=20)	# Mumbai
	country = models.CharField(blank=False, max_length=20)	# India
	loc_type= models.IntegerField('Type', blank=False, choices=LOCATION_TYPE_CHOICES, default=2)

	# Geographic Location
	lat  	= models.DecimalField('latitude' , null=True, blank=False, max_digits=10, decimal_places=8)	# 18.921836
	lng  	= models.DecimalField('longitude', null=True, blank=False, max_digits=10, decimal_places=8)	# 72.834705

	# Identification by third parties
	facebook_id		= models.CharField(null=True, blank=False, unique=True, max_length=30)	# 106632399377082
	foursquare_id 	= models.CharField(null=True, blank=False, unique=True, max_length=30)	# 4b0587d1f964a520cea222e3

	# Timestamps
	created_at	=	models.DateTimeField(auto_now_add=True) 
	updated_at	=	models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.name		 


# =====================================================================================================

class Photo(models.Model):
	
	link 		= models.TextField(blank=False, unique=True) 		# The web uri of the photo
	attribution = models.TextField(blank=True) 						# The photo may need to be attributed to someone
	is_deleted 	= models.BooleanField(default=False)				# If True, this photo should not be shown / used
	title		= models.TextField(blank=True) 
	
	# There can be one or more photos belonging to a location
	location 	= models.ForeignKey(Location, related_name='photos', related_query_name='photo')

	# Size
	height 		= models.IntegerField(null=True)
	width		= models.IntegerField(null=True)
	bytes		= models.IntegerField(null=True)

	# Timestamps
	created_at	=	models.DateTimeField(auto_now_add=True) 
	updated_at	=	models.DateTimeField(auto_now=True)


# =====================================================================================================