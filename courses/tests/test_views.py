#
import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

pytestmark = pytest.mark.django_db


class TestCourses(APITestCase):
    def test_course(self):
        response = self.client.get(reverse('courses'))
        self.assertIsInstance(response.data["posts"], list)

        sample_course = {"name": "English", "description": "Well we learn English", "branches": [{
            "latitude": 123123123,
            "longitude": 213213123,
            "address": "test"
        }], "contacts": [{"type": "123123", "value": "12312312"}]}
        response = self.client.post(reverse('courses'), sample_course, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.get(reverse('courses'))

        dict_lists = {
            "name": "English zone",
            "description": "Well we learn English"
        }
        name_values = {}
        for dict_list in dict_lists :
            for dictionary in dict_list :
                if 'name' in dictionary :
                    value = dictionary['name']
                    self.assertNotIn(value, dict_lists)
                    name_values.add(value)

