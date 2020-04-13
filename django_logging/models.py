from django.db import models
from django.utils.translation import gettext_lazy as _

import datetime


class Logging(models.Model):
    method = models.CharField(_('Method'), max_length=255)
    path = models.CharField(_('Path'), max_length=255)
    user = models.CharField(_('Path'), max_length=255)
    ip = models.CharField(_('IP'), max_length=255)
    time = models.CharField(_('Time'), max_length=255)
    status = models.CharField(_('Status'), max_length=255)
    length = models.CharField(_('Length'), max_length=255)
    content_type = models.CharField(_('Content Type'), max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta(object):
        verbose_name = _('Logging')
        verbose_name_plural = _('Loggin')

    def __unicode__(self):
        return str(self.path)

    def __str__(self):
        return str(self.path)
