from rest_framework.test import APITestCase
from rest_framework import status


class TestSetUp(APITestCase):

    def setUp(self):
        self.url = '/api/adn/mutant/'

    def test_adn_mutante(self):
        response = self.client.post(
            self.url,
            {
                "dna": ["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG"]
            },
            format='json'

        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_adn_human(self):
        response = self.client.post(
            self.url,
            {
                "dna": ["ATGCGA", "CAGTGC", "TTATTT", "AGACGG", "GCGTCA", "TCACTG"]
            },
            format='json'

        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_adn_null(self):
        response = self.client.post(
            self.url,
            {
                "dna": []
            },
            format='json'

        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_adn_not_array(self):
        response = self.client.post(
            self.url,
            {
                "dna": ""
            },
            format='json'

        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_adn_length(self):
        response = self.client.post(
            self.url,
            {
                "dna": ["ATGCGA"]

            },
            format='json'

        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_adn_reference(self):
        response = self.client.post(
            self.url,
            {
                "dna": ["ATGRGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG"]

            },
            format='json'

        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
