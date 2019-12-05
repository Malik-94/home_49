from rest_framework import serializers
from webapp.models import Project,Task


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('id', 'summary', 'description', 'status', 'type', 'project',  'created_at', 'update_at')


class ProjectSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ('id', 'summary', 'description', 'tasks', 'created_at', 'update_at')

