from django.urls import path
from webapp.views import IndexView, TaskCreateView, TaskUpdateView, TaskDeleteView, TaskView, StatusCreateView, \
    StatusUpdateView, StatusList, StatusDeleteView, TypeCreateView, TypeList, TypeUpdateView, TypeDeleteView, \
    ProjectListView

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('article/<int:pk>/', TaskView.as_view(), name='task_view'),
    path('articles/add/', TaskCreateView.as_view(), name='task_add'),
    path('article/<int:pk>/edit/', TaskUpdateView.as_view(), name='task_update'),
    path('article/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('status/', StatusList.as_view(), name='status_list'),
    path('statuses/add/', StatusCreateView.as_view(), name='status_add'),
    path('status/<int:pk>/edit/', StatusUpdateView.as_view(), name='status_update'),
    path('status/<int:pk>/delete/', StatusDeleteView.as_view(), name='status_delete'),
    path('type/', TypeList.as_view(), name='type_list'),
    path('types/add/', TypeCreateView.as_view(), name='type_add'),
    path('type/<int:pk>/edit/', TypeUpdateView.as_view(), name='type_update'),
    path('type/<int:pk>/delete/', TypeDeleteView.as_view(), name='type_delete'),
    path('projects/', ProjectListView.as_view(), name='project_list'),


]