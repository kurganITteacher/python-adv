from django.db import models

from authapp.models import UserProfile


class Project(models.Model):
    name = models.CharField(max_length=128, unique=True)
    owner = models.ForeignKey('authapp.UserProfile', on_delete=models.PROTECT,
                              related_name='projects',
                              related_query_name='projects')
    desc = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    members = models.ManyToManyField('authapp.UserProfile')

    def __str__(self):
        return f'{self.name}'


class ProjectTask(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    text = models.TextField()
    author = models.ForeignKey('authapp.UserProfile', on_delete=models.CASCADE,
                               related_name='tasks',
                               related_query_name='projects_tasks')
    executors = models.ManyToManyField('authapp.UserProfile')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.project}: {self.title}'
