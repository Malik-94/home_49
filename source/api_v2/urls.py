from django.urls import include, path
from rest_framework import routers
from .views import ProjectViewSet, TaskViewSet

router = routers.DefaultRouter()
router.register(r'Project', ProjectViewSet)
router.register(r'Task', TaskViewSet)


app_name = 'api_v2'

urlpatterns = [

    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]