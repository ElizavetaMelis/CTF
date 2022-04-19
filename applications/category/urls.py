from django.urls import path

from applications.category.views import CategoryViewSet



from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', CategoryViewSet)

urlpatterns = []

urlpatterns.extend(router.urls)