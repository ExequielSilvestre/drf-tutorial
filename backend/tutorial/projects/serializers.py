from rest_framework import serializers
from projects.models import Projects, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User
from rest_framework import permissions

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['id', 'name', 'active', 'finish_date', 'owner', 'permissions_classes']
        read_only_fields = ['id']
        extra_kwargs = {
            'active': {'default': True},
        }
        owner = serializers.ReadOnlyField(source='owner.username')

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Projects.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets', 'permissions_classes']
