# Django
from django.test import TestCase
from django.core.management import call_command

# DRF
from rest_framework.test import APIClient
from rest_framework import status

# Models
from domain.models import Employee, Department

# import json


class TestEmployeeAPI(TestCase):

    def setUp(self):
        # Set up fake data
        call_command('loaddata', 'seeds/auth', verbosity=0)
        call_command('loaddata', 'seeds/department', verbosity=0)
        call_command('loaddata', 'seeds/employee', verbosity=0)

        self.client = APIClient()

    def test_get_employees(self):
        endpoint = '/api/v1/employee'
        response = self.client.get(endpoint)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_response = [
            {
                "department": {
                    "id": 1,
                    "name": "Architecture"
                },
                "email": "arnaldo@luizalabs.com",
                "id": 1,
                "name": "Arnaldo Pereira"
            },
            {
                "department": {
                    "id": 2,
                    "name": "E-commerce"
                },
                "email": "renato@luizalabs.com",
                "id": 2,
                "name": "Renato Pedigoni"
            },
            {
                "department": {
                    "id": 3,
                    "name": "Mobile"
                },
                "email": "catoto@luizalabs.com",
                "id": 3,
                "name": "Thiago Catoto"
            }
        ]
        response_dict = response.json()
        self.assertEqual(len(response_dict), 3)
        for employee in response_dict:
            self.assertTrue(employee in expected_response)

    def test_post_employee(self):
        endpoint = '/api/v1/employee/'
        payload = {
            'name': 'Joabe Mendes',
            'email': 'joabe.mdl@gmail.com',
            'department': Department.objects.first().id
        }
        response = self.client.post(endpoint, data=payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response_dict = response.json()
        self.assertEqual(response_dict['name'], payload['name'])
        self.assertEqual(response_dict['email'], payload['email'])
        self.assertEqual(
            response_dict['department'],
            Department.objects.first().id
        )

    def test_post_employee_email_validation_failure(self):
        endpoint = '/api/v1/employee/'
        payload = {
            'name': 'Joabe Mendes',
            'email': 'not an email',
            'department': Department.objects.first().id
        }
        response = self.client.post(endpoint, data=payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertDictEqual(
            {
                "email": [
                    "Enter a valid email address."
                ]
            },
            response.json()
        )

    def test_post_employee_existing_email_validation_failure(self):
        endpoint = '/api/v1/employee/'
        payload = {
            'name': 'Joabe Mendes',
            'email': Employee.objects.first().email,
            'department': Department.objects.first().id
        }
        response = self.client.post(endpoint, data=payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertDictEqual(
            {
                "email": [
                    "This field must be unique."
                ]
            },
            response.json()
        )
        # print(json.dumps(response.json(), indent=4, sort_keys=True))

    def test_put_employee(self):
        endpoint = '/api/v1/employee/'
        endpoint += str(Employee.objects.first().id)
        payload = {
            'name': 'Another name',
            'email': 'email@mail.com',
            'department': Department.objects.last().id
        }
        response = self.client.put(endpoint, data=payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_dict = response.json()
        self.assertEqual(response_dict['name'], payload['name'])
        self.assertEqual(response_dict['email'], payload['email'])
        self.assertEqual(response_dict['department'], payload['department'])

    def test_delete_employee(self):
        id = Employee.objects.first().id
        endpoint = '/api/v1/employee/' + str(id)
        response = self.client.delete(endpoint)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Employee.objects.count(), 2)
        self.assertRaises(
            Employee.DoesNotExist, lambda: Employee.objects.get(pk=id)
        )
