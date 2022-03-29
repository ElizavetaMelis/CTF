from django.contrib import admin
from django.utils.safestring import mark_safe

from applications.tasks.models import TaskImage, Task


class InlineTaskImage(admin.TabularInline):
    model = TaskImage
    extra = 1
    fields = ['image', ]

class TaskAdminDisplay(admin.ModelAdmin):
    inlines = [InlineTaskImage, ]
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

