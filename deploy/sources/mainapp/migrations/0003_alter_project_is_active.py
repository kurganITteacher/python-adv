# Generated by Django 3.2.7 on 2021-10-18 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20211018_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='is_active',
            field=models.BooleanField(db_index=True, default=True),
        ),
    ]
