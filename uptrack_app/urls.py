from rest_framework_nested import routers
from django.conf.urls import url, include
from uptrack_app.viewset import ProjectViewSet, UpdateViewSet

router = routers.SimpleRouter()
router.register(r'projects', ProjectViewSet,base_name='projects')
projects_router = routers.NestedSimpleRouter(router, r'projects', lookup='project')
projects_router.register(r'updates', UpdateViewSet, base_name='project-updates')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(projects_router.urls)),
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework'))
]
