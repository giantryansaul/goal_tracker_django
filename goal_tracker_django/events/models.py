from django.db import models

from ..core.models import TimeStampedUserModel


class EventManager(models.Manager):
    """
    Manager for event model.
    """

    use_for_related_fields = True


class Event(TimeStampedUserModel):
    """
    Model for Events. Inherits user and create/modified dates from
        TimeStampedModel.

    note (CharField): optional description of event
    logged_date (DateTimeField): editable date of field,
        automatically set on creation.
    associated_goal (ForeignKey): relationship to the associated
        goal.
    """
    note = models.CharField(max_length=255)
    logged_date = models.DateTimeField(auto_now=True)
    associated_goal = models.ForeignKey
