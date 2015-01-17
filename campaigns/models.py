from django.db import models
from django.conf import settings

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

class Campaign(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(AUTH_USER_MODEL)

class Session(models.Model):
    campaign = models.ForeignKey(Campaign)
    number = models.IntegerField()

class Thread(models.Model):
    campaign = models.ForeignKey(Campaign)
    name = models.CharField(max_length=100)

class Event(models.Model):
    campaign = models.ForeignKey(Campaign)
    session = models.ForeignKey(Session)
    threads = models.ManyToManyField(Thread)
    content = models.TextField()

