from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import UpdateView, DeleteView
from django.views.generic import TemplateView
from webapp.forms import TaskForm, SimpleSearchForm
from webapp.models import Task
from django.views.generic import ListView,CreateView


class IndexView(ListView):
    context_object_name = 'task'
    model = Task
    template_name = 'task/index.html'
    ordering = ['created_at']
    paginate_by = 2
    paginate_orphans = 1

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = SimpleSearchForm(self.request.GET)
        return context


    def get_queryset(self):
        queryset = super().get_queryset()
        form = SimpleSearchForm(self.request.GET)
        if form.is_valid():
            query = form.cleaned_data['search']
            if query:
                queryset = queryset.filter(Q(description__icontains=query)|Q(summary__icontains=query))
        return queryset


class TaskView(TemplateView):
    template_name = 'task/task.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task_pk = kwargs.get('pk')
        context['task'] = get_object_or_404(Task, pk=task_pk)
        return context


class TaskCreateView(CreateView):
    template_name = 'task/create.html'
    form_class = TaskForm
    model = Task
    context_object_name = 'task'

    def get_success_url(self):
        return reverse('index')


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'task/update.html'
    context_object_name = 'task'
    form_class = TaskForm

    def get_success_url(self):
        return reverse ('task_view', kwargs={'pk': self.object.pk})


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task/delete.html'
    context_key = 'task'

    def get_success_url(self):
        return reverse('index')

