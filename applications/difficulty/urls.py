from django.urls import path

from applications.difficulty.views import DifficultyViewSet


from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', DifficultyViewSet)
urlpatterns = []

urlpatterns.extend(router.urls)