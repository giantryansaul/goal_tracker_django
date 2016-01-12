from django.db import models
from django.conf import settings


class TimeStampedUserModel(models.Model):
    """
    Abstraction base class model for updating `created` and `modified` fields.
    """
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    class Meta:
        abstract = True