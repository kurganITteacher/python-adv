from django.db import models, transaction, DatabaseError

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
    is_active = models.BooleanField(default=True, db_index=True)

    def __str__(self):
        return f'{self.name}'

    def restore(self):
        self.is_active = True
        self.name = self.name[1:]
        self.projecttask_set.all().update(is_active=True)
        self.save()
        return self

    def delete(self, using=None, keep_parents=False):
        with transaction.atomic() as _:
            self.is_active = False
            self.name = f'_{self.name}'
            self.projecttask_set.all().update(is_active=False)  # db level
            # raise DatabaseError
            self.save()
        return 1, {}  # to fix


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
    is_active = models.BooleanField(default=True, db_index=True)

    def __str__(self):
        return f'{self.project}: {self.title}'

# author.tasks.all()
