from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView
from webapp.models import Status
from webapp.forms import StatusForm
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin



class StatusList( LoginRequiredMixin, ListView):
    context_object_name = 'status'
    model = Status
    template_name = 'status/status.html'

    def get_success_url(self):
        return reverse('index')


class StatusCreateView(LoginRequiredMixin, CreateView):
    model = Status
    template_name = 'status/status_create.html'
    context_object_name = 'status'
    form_class = StatusForm

    def get_success_url(self):
        return reverse('status_list')


class StatusUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'status/status_update.html'
    model = Status
    form_class = StatusForm
    context_object_name = 'status'

    def get_success_url(self):
        return reverse('status_list')


class StatusDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'status/status_delete.html'
    model = Status
    context_object_name = 'status'

    def get_success_url(self):
        return reverse('index')


