from django.test import TestCase
from util import gcs
# Create your tests here.

class GoogleSearchTestCase(TestCase):
	def setUp(self):
		pass

	def test_can_search_without_query(self):
		""" The Google search fails without the query param """
		self.assertRaises(Exception, gcs.search())

	def test_can_search_with_query(self):
		""" The Google search returns results when a query is specified """
		print gcs.search(q="Santorini, Greece")