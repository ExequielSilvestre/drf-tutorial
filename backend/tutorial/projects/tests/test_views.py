from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status

class TestProjectViews(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create(username='testuser')
        cls.client = APIClient()
        cls.client.force_authenticate(user=cls.user)

    def test_project_list(self):
        response = self.client.get(reverse('project-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    