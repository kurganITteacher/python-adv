from django.db import models


class TeachGroup(models.Model):
    title = models.CharField(max_length=64)
    desc = models.TextField(blank=True)


class Student(models.Model):
    teach_group = models.ForeignKey(TeachGroup, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    date_birth = models.DateField(null=True)
