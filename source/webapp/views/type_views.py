from django.urls import reverse
from django.views.generic import UpdateView, CreateView, DeleteView
from webapp.models import Type
from webapp.forms import TypeForm
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin


class TypeList( LoginRequiredMixin,ListView):
    context_object_name = 'types'
    model = Type
    template_name = 'type/type.html'

    def get_success_url(self):
        return reverse('webapp:index')



class TypeCreateView(LoginRequiredMixin, CreateView):
    template_name = 'type/type_create.html'
    context_object_name = 'type'
    form_class = TypeForm

    def get_success_url(self):
        return reverse('status_list')




class TypeUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'type/type_update.html'
    model = Type
    form_class = TypeForm
    context_object_name = 'type'

    def get_success_url(self):
        return reverse('status_list')



class TypeDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'type/type_delete.html'
    model = Type
    context_object_name = 'type'

    def get_success_url(self):
        return reverse('webapp:index')






