from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, TemplateView
from webapp.forms import TaskForm
from webapp.models import Task


class IndexView(View):
    def get(self, request, *args, **kwargs):
        task = Task.objects.all()
        return render(request, 'index.html', context={
            'task': task
        })

class TaskView(View):
    def get (self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        return render(request, 'task.html', context={
            'task': task
        })

class TaskCreateView(View):
    def get (self,request, *args, **kwargs):
        if request.method == 'GET':
            form = TaskForm()
            return render(request, 'create.html', context={'form': form})

    def post (self, request, *args, **kwargs):
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task = Task.objects.create(
            summary=form.cleaned_data['summary'],
            description=form.cleaned_data['description'],
            status=form.cleaned_data['status'],
            type=form.cleaned_data['type'],
            # created_at = form.cleaned_data['created_at']
            )
            return redirect('task_view', pk=task.pk)
        else:
            return render(request, 'create.html', context={'form': form})

class TaskUpdateView(View):
    def get (self, request, pk, *args, **kwargs):
        task = get_object_or_404(Task, pk=pk)
        if request.method == 'GET':
            form = TaskForm(data={
                'summary': task.summary,
                'created_at': task.created_at,
                'description': task.description,
                'type': task.type,
                'status': task.status
            })
            return render(request, 'update.html', context={'form': form, 'task': task})

    def post (self, request, pk, *args, **kwargs):
            form = TaskForm(data=request.POST)
            task = get_object_or_404(Task, pk=pk)
            if form.is_valid():
                task.summary = form.cleaned_data['summary']
                task.description = form.cleaned_data['description']
                task.type = form.cleaned_data['type']
                task.status = form.cleaned_data['status']
                task.save()
                return redirect('task_view', pk=task.pk)
            else:
                return render(request, 'update.html', context={'form': form, 'task': task})


class TaskDeleteView(View):
    def get (self,request , pk, *args, **kwargs):
        task = get_object_or_404(Task, pk=pk)
        if request.method == 'GET':
            return render(request, 'delete.html', context={'task': task})

    def post (self,request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get('pk'))
        task.delete()
        return redirect('index')
