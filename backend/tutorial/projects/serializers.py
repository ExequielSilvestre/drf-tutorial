from rest_framework import serializers
from projects.models import Projects, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User
from rest_framework import permissions

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Projects
        fields = ['id', 'name', 'active', 'finish_date', 'owner']
        read_only_fields = ['id']
        extra_kwargs = {
            'active': {'default': True},
        }

class UserSerializer(serializers.HyperlinkedModelSerializer):
    projects = serializers.HyperlinkedRelatedField(many=True, view_name='project-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'projects']
