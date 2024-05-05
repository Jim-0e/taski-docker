"""Admin."""
from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    """Админка панели."""

    list_display = ('title', 'description', 'completed')


admin.site.register(Task, TaskAdmin)
