# Django
from django.test import TestCase
from django.core.management import call_command

# DRF
from rest_framework.test import APIClient
from rest_framework import status


class TestEmployeeAPI(TestCase):

    def setUp(self):
        # Set up fake data
        call_command('loaddata', 'seeds/auth', verbosity=0)
        call_command('loaddata', 'seeds/department', verbosity=0)
        call_command('loaddata', 'seeds/employee', verbosity=0)

        self.client = APIClient()

    def test_get_employees(self):
        endpoint = '/api/v1/department'
        response = self.client.get(endpoint)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_response = [
            {
                "id": 1,
                "name": "Architecture"
            },
            {
                "id": 2,
                "name": "E-commerce"
            },
            {
                "id": 3,
                "name": "Mobile"
            }
        ]
        response_dict = response.json()
        self.assertEqual(len(response_dict), 3)
        for employee in response_dict:
            self.assertTrue(employee in expected_response)
