from django.views.generic import ListView
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from mainapp.models import Project, ProjectTask
from mainapp.serializers import ProjectSerializer, ProjectTaskSerializer


class ProjectList(ListView):
    model = Project


class ProjectTaskList(ListView):
    model = ProjectTask


class ProjectViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    # queryset = Project.objects.all()
    queryset = Project.objects.filter(is_active=True)
    serializer_class = ProjectSerializer


class ProjectTaskViewSet(ModelViewSet):
    queryset = ProjectTask.objects.all()
    serializer_class = ProjectTaskSerializer
