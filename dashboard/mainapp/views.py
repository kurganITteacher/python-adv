from django.views.generic import ListView
from mainapp.serializers import ProjectSerializer
from rest_framework.viewsets import ModelViewSet

from mainapp.models import Project, ProjectTask


class ProjectList(ListView):
    model = Project


class ProjectTaskList(ListView):
    model = ProjectTask


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

# class ProjectTaskViewSet():
#     pass
