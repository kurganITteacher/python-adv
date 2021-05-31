from django.shortcuts import render

from mainapp.models import TeachGroup


def index(request):
    teach_groups = TeachGroup.objects.all()
    context = {
        'page_title': 'список групп',
        'teach_groups': teach_groups
    }
    return render(request, 'mainapp/index.html', context=context)


def teach_group_create(request):
    if request.method == 'POST':
        form = None
    else:
        form = None
    context = {
        'page_title': 'новая группа',
        'form': form
    }
    return render(request, 'mainapp/teach_group_form.html', context=context)
