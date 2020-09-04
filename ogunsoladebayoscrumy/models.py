from django.db import models
from django.contrib.auth.models import User

# Create your models here.
...


class GoalStatus(models.Model):
    status_name = models.CharField(max_length=255)

    def __str__(self):
        return self.status_name

    class Meta:
        verbose_name_plural = 'GoalStatus'


class ScrumyGoals(models.Model):
    goal_name = models.CharField(max_length=255)
    goal_id = models.IntegerField(unique=True)
    created_by = models.CharField(max_length=255)
    moved_by = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)
    goal_status = models.ForeignKey(GoalStatus, on_delete=models.PROTECT)
    user = models.ForeignKey(User, related_name='user',
                             on_delete=models.PROTECT)

    def __str__(self):
        return self.goal_name

    class Meta:
        verbose_name_plural = 'ScrumyGoals'
    ...


class ScrumyHistory(models.Model):
    moved_by = models.CharField(max_length=255)
    created_by = models.CharField(max_length=255)
    moved_from = models.CharField(max_length=255)
    moved_to = models.CharField(max_length=255)
    time_of_action = models.DateTimeField()
    goal = models.ForeignKey(ScrumyGoals, on_delete=models.PROTECT)

    def __str__(self):
        return self.created_by

    class Meta:
        verbose_name_plural = 'ScrumyHistory'
    ...
