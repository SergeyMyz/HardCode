from rest_framework import routers
from .api import ViewSet, LessonsSet

router = routers.DefaultRouter()
router.register('api/test', ViewSet, 'TEST')
router.register('api/2', LessonsSet, 'TEST2')

urlpatterns = router.urls
