from rest_framework import serializers
from webapp.models import Project,Task


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('id', 'summary', 'description', 'created_at','update_at')


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('id', 'summary', 'description', 'status', 'type', 'project',  'created_at', 'update_at')