from rest_framework import viewsets
from rest_framework.response import Response
from uptrack_app.models import Project, Update
from uptrack_app.serializers import ProjectSerializer, UpdateSerializer
from rest_framework.views import APIView
from django.db.models import Count

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class UpdateViewSet(viewsets.ModelViewSet):
    queryset = Update.objects.all()
    serializer_class = UpdateSerializer
    def list(self, request, project_pk=None):
        queryset = Update.objects.filter( project = project_pk )
        serializer = UpdateSerializer( queryset, many = True )
        return Response(serializer.data)

class UpdateCountView(APIView):
    def get(self, request):
        count = Update.objects.values("project__name").annotate(update = Count("project"))
        return Response(count)
