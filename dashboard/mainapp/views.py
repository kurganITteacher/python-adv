from django.views.generic import ListView
from rest_framework.viewsets import ModelViewSet

from mainapp.models import Project, ProjectTask
from mainapp.serializers import ProjectSerializer, ProjectTaskSerializer


class ProjectList(ListView):
    model = Project


class ProjectTaskList(ListView):
    model = ProjectTask


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectTaskViewSet(ModelViewSet):
    queryset = ProjectTask.objects.all()
    serializer_class = ProjectTaskSerializer
