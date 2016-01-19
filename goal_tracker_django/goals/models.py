from django.db import models

from ..core.models import TimeStampedUserModel


class GoalManager(models.Manager):
    """
    Manager for goal model.
    """

    use_for_related_fields = True


class Goal(TimeStampedUserModel):
    """
    Model for Goals. Inherits user and created/modified dates from
    TimeStampedModel.


    """
    STATUSES = [
        ('INPROGRESS', 'In Progress'),
        ('UNFINISHED', 'Unfinished'),
        ('FINISHED', 'Finished')
    ]

    date = models.DateTimeField()
    amount = models.IntegerField()
    name = models.CharField(max_length=255)
    status = models.CharField(choices=STATUSES)