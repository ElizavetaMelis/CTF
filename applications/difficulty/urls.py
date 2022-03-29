from django.urls import path

from applications.difficulty.views import DifficultyListView

urlpatterns = [
    path('', DifficultyListView.as_view()),
]