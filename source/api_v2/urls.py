from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from .views import ProjectViewSet, TaskViewSet

router = routers.DefaultRouter()
router.register(r'Project', ProjectViewSet)
router.register(r'Task', TaskViewSet)


app_name = 'api_v2'

urlpatterns = [

    path('', include(router.urls)),
    path('login/', obtain_auth_token, name='api_token_auth')

]