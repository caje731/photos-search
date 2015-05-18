from django.test import TestCase
from util import gcs
# Create your tests here.

class GoogleSearchTestCase(TestCase):
	def setUp(self):
		pass

	def test_can_search_without_query(self):
		""" The Google search fails without the query param """
		self.assertRaises(Exception, gcs.search())