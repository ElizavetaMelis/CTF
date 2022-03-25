from django.urls import path

from applications.difficulty.views import DifficultyListView

urlpatterns = [
    path('difficulty/', DifficultyListView.as_view()),
]