from django.contrib import admin

from applications.tasks.models import Task

admin.site.register(Task)
