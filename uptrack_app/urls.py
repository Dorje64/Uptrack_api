from rest_framework import routers
from django.conf.urls import url, include
from uptrack_app.viewset import ProjectViewSet, UpdateViewSet

router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet,base_name='projects')
router.register(r'updates', UpdateViewSet, base_name='updates')
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework'))
]
