from rest_framework.routers import DefaultRouter

from applications.testing.views import TestingViewSet

router = DefaultRouter()
router.register('', TestingViewSet)

urlpatterns = []
urlpatterns.extend(router.urls)