from django.views.generic import ListView
from webapp.models import Project


class ProjectListView(ListView):
    context_object_name = 'projects'
    model = Project
    template_name = 'project/project_list.html'
    ordering = ['created_at']
