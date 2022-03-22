"""Models for Studyspace app"""
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

SPACE_TYPE_CHOICES = (
    ('open', 'Open'),
    ('part', 'Partly closed off'),
    ('closed_small', 'Separate room (max 2 persons)'),
    ('closed_big', 'Separate room (max 7 persons)'),
)


class Space(models.Model):
    """ Study spaces to choose from """
    name = models.CharField(max_length=25, unique=True, blank=True)
    max_capacity = models.IntegerField(default=1, null=False, blank=False)
    type = models.CharField(
        choices=SPACE_TYPE_CHOICES,
        default='open',
        max_length=25)
    available_tech = models.TextField(max_length=100, blank=True, null=True)

    def __str__(self):
        if not self.name:
            self.name = f'Room {self.id}'  # not an issue
            self.save()
        return self.name


class Reservation(models.Model):
    """ Model for a reserved time slot at a study space """
    username = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reservations')
    start = models.DateTimeField(null=False, blank=False, default=timezone.now)
    space = models.ForeignKey(
        Space,
        on_delete=models.CASCADE,
        null=False,
        blank=False)
    snacks_discount = models.BooleanField(default=False)
    last_changed = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta class for Reservation"""
        ordering = ['-start']

    def __str__(self):
        return f'{self.start} - {self.space}'
