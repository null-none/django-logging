from django.contrib import admin

from .models import Logging


class LoggingAdmin(admin.ModelAdmin):
    fields = ('method', 'path', 'user', 'ip', 'time', 'status', 'length')
    list_filter = ('method', 'status')
    date_hierarchy = 'created_date'


admin.site.register(Logging, LoggingAdmin)
