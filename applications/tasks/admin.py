from django.contrib import admin
from django.utils.safestring import mark_safe

from applications.tasks.models import Task


class TaskAdminDisplay(admin.ModelAdmin):
    list_display = ('category', 'difficulty', 'hint', 'description')
    search_fields = ('category', 'description')
    list_filter = ('category', 'difficulty')

    def image(self, obj):
        img = obj.image.first()
        if img:
            return mark_safe(f'<img src="{img.image.url}" width="80" height="80" style="object-fit: contain" />')
        else:
            return ''


admin.site.register(Task, TaskAdminDisplay)

