from django.views.generic import ListView
from webapp.forms import SimpleSearchForm
from webapp.models import Project


class ProjectListView(ListView):
    context_object_name = 'projects'
    model = Project
    template_name = 'project/project_list.html'
    ordering = ['created_at']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        print(context)
        context['form'] = SimpleSearchForm(self.request.GET)
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        form = SimpleSearchForm(self.request.GET)
        if form.is_valid():
            query = form.cleaned_data['search']
            if query:
                queryset = queryset.filter(Q(description__icontains=query) | Q(summary__icontains=query))
        return queryset
