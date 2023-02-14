from test.factories import test_page_factory
from test.testapp.models import HomePage, PanoramaPage, TourPage

from django.test import TestCase


class TestTestModels(TestCase):
    def setUp(self):
        self.home_page, self.tour_page, self.panorama_page = test_page_factory()

    def test_home_page(self):
        self.assertIsInstance(self.home_page, HomePage)

    def test_tour_page(self):
        self.assertIsInstance(self.tour_page, TourPage)

    def test_panorama_page(self):
        self.assertIsInstance(self.panorama_page, PanoramaPage)
