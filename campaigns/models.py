from django.db import models
from django.conf import settings

from ordered_model.models import OrderedModel

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

class Campaign(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(AUTH_USER_MODEL)

    def __str__(self):
        return '{}\'s {}'.format(self.owner, self.name)

class Session(models.Model):
    campaign = models.ForeignKey(Campaign)
    number = models.IntegerField()

    def __str__(self):
        return '{} - Session {}'.format(self.campaign.__str__(), self.number)

class Event(OrderedModel):
    campaign = models.ForeignKey(Campaign)
    session = models.ForeignKey(Session)
    content = models.TextField(blank=True)

    def __str__(self):
        return '{} - "{}..."'.format(self.campaign.__str__(), self.content[:50])

class Note(OrderedModel):
    campaign = models.ForeignKey(Campaign)
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    public = models.BooleanField(default=False)

    def __str__(self):
        return '{} - {}'.format(self.campaign.__str__(), self.title)

