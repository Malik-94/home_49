from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from accounts.views import register_view, UserDetailView,UserListView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register_view, name='register'),
    path('profile/<pk>/', UserDetailView.as_view(), name='user_detail'),
    path('change/', UserListView.as_view(), name='user_list')
]

app_name = 'accounts'
