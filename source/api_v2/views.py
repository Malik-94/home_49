from rest_framework import viewsets
from rest_framework.permissions import SAFE_METHODS
from webapp.models import Project,Task
from api_v2.serializers import ProjectSerializer, TaskSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return []

        return super().get_permissions()


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return []

        return super().get_permissions()


