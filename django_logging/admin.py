from django.contrib import admin

from .models import Logging


class LoggingAdmin(admin.ModelAdmin):
    pass


admin.site.register(Logging, LoggingAdmin)