from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from applications.account.models import User
from applications.tasks.models import Task


class Testing(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='testing')
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='testing')
    flag = models.TextField()



    def __str__(self):
        return self.title



