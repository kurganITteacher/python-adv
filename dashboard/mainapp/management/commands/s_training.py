import json
from datetime import datetime

from django.core.management.base import BaseCommand

from mainapp.models import Project


def project_serializer(project):
    # print(type(project), vars(project))
    # result = vars(project)
    result = {k: v
              for k, v in vars(project).items()
              if not k.startswith('_')}
    for k, v in result.items():
        if isinstance(v, datetime):
            # print('dt', v.strftime("%Y-%m-%d %H:%M"))
            result[k] = v.strftime("%Y-%m-%d %H:%M")
    for k, v in result.items():
        if k.endswith('_id'):
            print('foreign', k, v, type(v))  # owner_serializer()

    # result = json.dumps(result, default=str)
    result = json.dumps(result)
    return result


class Command(BaseCommand):
    def handle(self, *args, **options):
        for project in Project.objects.all():
            # print(type(project), project.__dict__)
            # print(type(project), vars(project))
            p_as_str = project_serializer(project)
            print(type(p_as_str))
            print(p_as_str)
