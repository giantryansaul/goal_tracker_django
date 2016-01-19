from django.contrib import admin

from .models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = (
        "note",
        "logged_date",
        "associated_goal",
    )


admin.site.register(Event, EventAdmin)