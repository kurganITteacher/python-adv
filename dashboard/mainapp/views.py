from django.views.generic import ListView

from mainapp.models import Project, ProjectTask


# def projects_view(request):
#     projects = Project.objects.all()
#     return render(request, 'mainapp/projects.html', {'projects': projects})
#
#
# def project_tasks_view(request):
#     project_tasks = ProjectTask.objects.all()
#     return render(request, 'mainapp/project_tasks.html', {'project_tasks': project_tasks})


class ProjectList(ListView):
    model = Project
    # template_name = 'mainapp/projects.html'
    # context_object_name = 'projects'


class ProjectTaskList(ListView):
    model = ProjectTask
