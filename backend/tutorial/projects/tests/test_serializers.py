import datetime
from django.contrib.auth.models import User
from django.test import TestCase
from projects.serializers import ProjectSerializer
from projects.models import Projects

class ProjectSerializerTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create(username='testuser')

    def setUp(self):
        self.project = Projects.objects.create(
            name='Test Project',
            active=True,
            owner=self.user,
            finish_date='2020-01-01',
        )

    def test_project_serializer_valid_data(self):
        data = {
            'id': self.project.id,
            'name': 'Test Project',
            'active': True,
            'finish_date': '2020-01-01',
            'owner': self.user.id,  # Pasar el ID del usuario en lugar del objeto de usuario
        }
        serializer = ProjectSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_project_serializer_invalid_data(self):
        data = {
            # Missing required 'name' field
            'active': True,
            'finish_date': '2020-01-01',
            'owner': self.user.id,
        }
        serializer = ProjectSerializer(data=data)
        self.assertFalse(serializer.is_valid())

    def test_project_serializer_update(self):
        updated_data = {
            'name': 'Updated Test Project',
            'finish_date': '2021-01-01',
        }
        serializer = ProjectSerializer(instance=self.project, data=updated_data, partial=True)
        self.assertTrue(serializer.is_valid())
        updated_project = serializer.save()
        self.assertEqual(updated_project.name, 'Updated Test Project')
        expected_date = datetime.date(2021, 1, 1)
        self.assertEqual(updated_project.finish_date, expected_date)
