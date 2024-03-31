
from projects.models import Projects


from django.test import TestCase
from django.contrib.auth.models import User


class ProjectsModelTest(TestCase):
    def setUp(self):
        user = User.objects.create(username='testuser')
        self.project = Projects.objects.create(
            name='Test Project',
            active=True,
            owner=user,
            finish_date='2020-01-01',
        )

    def test_project_was_created(self):
        self.assertEqual(self.project.name, 'Test Project')
        self.assertTrue(self.project.active)
        self.assertEqual(self.project.owner.username, 'testuser')            
        self.assertEqual(self.project.finish_date, '2020-01-01')

    
