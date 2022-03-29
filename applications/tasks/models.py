from django.db import models

from applications.category.models import Category
from applications.difficulty.models import Difficulty


class Task(models.Model):
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL, related_name='task')
    difficulty = models.ForeignKey(Difficulty, null=True, on_delete=models.SET_NULL, related_name='task')
    description = models.TextField()
    hint = models.TextField()
    level = models.TextField()
    point = models.PositiveIntegerField()


    def __str__(self):
        return str(self.category)


class TaskImage(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='image')
    image = models.ImageField(upload_to='')

    def __str__(self):
        return str(self.task.category)