# Generated by Django 3.2.7 on 2021-10-18 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='projecttask',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]