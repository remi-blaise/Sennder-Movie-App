from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .views import retrieveMoviesFromGhibliAPI


class MoviesTests(TestCase):
    def test_is_ghibli_api_request_working(self):
        """
        Check every movie's people key is filled.
        """

        films = retrieveMoviesFromGhibliAPI()
        self.assertIs(type(films), list)

        for film in films:
            self.assertTrue('people' in film)

    def test_is_movies_page_running(self):
        """
        Check /movies is running
        """

        response = self.client.get('/movies/')
        self.assertEquals(response.status_code, 200)
