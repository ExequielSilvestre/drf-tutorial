from rest_framework import serializers
from projects.models import Projects, LANGUAGE_CHOICES, STYLE_CHOICES

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['id', 'name', 'active', 'finish_date']
        read_only_fields = ['id']
        extra_kwargs = {
            'active': {'default': True},
        }