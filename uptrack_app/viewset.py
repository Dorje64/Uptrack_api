from rest_framework import viewsets
from uptrack_app.models import Project, Update
from uptrack_app.serializers import ProjectSerializer, UpdateSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class UpdateViewSet(viewsets.ModelViewSet):
    queryset = Update.objects.all()
    serializer_class = UpdateSerializer
