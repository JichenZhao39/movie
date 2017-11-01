from django.test import TestCase
 
class SimpleTest(TestCase):
    def test_details(self):
        response = self.client.get('/movie/movies/detail/')
        self.assertEqual(response.status_code, 200)
 
    def test_list(self):
        response = self.client.get('/movie/movies/list/')
        self.assertEqual(response.status_code, 200)