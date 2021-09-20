from django.shortcuts import render

from mainapp.models import Project, ProjectTask


def projects_view(request):
    projects = Project.objects.all()
    return render(request, 'mainapp/projects.html', {'projects': projects})


def project_tasks_view(request):
    project_tasks = ProjectTask.objects.all()
    return render(request, 'mainapp/project_tasks.html', {'project_tasks': project_tasks})

