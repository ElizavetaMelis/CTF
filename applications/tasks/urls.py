from django.urls import path
from applications.tasks.views import TaskDetailView, FavoriteView, TaskViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', TaskViewSet)

urlpatterns = [
    path('<int:pk>/', TaskDetailView.as_view()),
    path('<int:pk>/favorite/', FavoriteView.as_view()),
]

urlpatterns.extend(router.urls)