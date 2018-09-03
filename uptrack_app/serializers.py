from uptrack_app.models import Project, Update
from rest_framework import serializers

class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ( 'id', 'name', 'repo_dir', 'created_at')

class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Update
        fields = ( 'id', "text", 'created_at', 'updated_at', 'project')
