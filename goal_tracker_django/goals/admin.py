from django.contrib import admin

from .models import Goal


class GoalAdmin(admin.ModelAdmin):
    list_display = (
        "date",
        "amount",
        "name",
        "status",
    )


admin.site.register(Goal, GoalAdmin)