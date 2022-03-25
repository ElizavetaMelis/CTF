from django.db import models

from applications.category.models import Category
from applications.difficulty.models import Difficulty


class Task(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL, related_name='task')
    difficulty = models.ForeignKey(Difficulty, null=True, on_delete=models.SET_NULL, related_name='task')
    description = models.TextField()
    hint = models.TextField()
    level = models.TextField()
    point = models.PositiveIntegerField()
    flag = models.CharField(max_length=255)


    def __str__(self):
        return self.title
