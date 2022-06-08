from rest_framework.test import APITestCase
from rest_framework import status


class TestSetUp(APITestCase):

    def setUp(self):
        self.url = '/mutant/'

    def test_adn_null(self):
        response = self.client.post(
            self.url,
            {
                "dna": []
            },
            format='json'

        )
        self.assertEqual(response.status_code,status.HTTP_404_NOT_FOUND)

    def test_adn_not_array(self):
        response = self.client.post(
            self.url,
            {
                "dna": ""
            },
            format='json'

        )
        self.assertEqual(response.status_code,status.HTTP_404_NOT_FOUND)


    def test_adn_length(self):
        response = self.client.post(
            self.url,
            {
                "dna": ""
            },
            format='json'

        )
        self.assertEqual(response.status_code,status.HTTP_404_NOT_FOUND)


