from rest_framework.serializers import ModelSerializer, StringRelatedField

from mainapp.models import Project, ProjectTask


class ProjectSerializer(ModelSerializer):
    # user = StringRelatedField()

    class Meta:
        model = Project
        fields = '__all__'


class ProjectTaskSerializer(ModelSerializer):
    class Meta:
        model = ProjectTask
        fields = '__all__'
