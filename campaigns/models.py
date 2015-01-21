from django.db import models
from django.conf import settings

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

class Thread(models.Model):
    campaign = models.ForeignKey(Campaign)
    name = models.CharField(max_length=100)

    def __str__(self):
        return '{} - {}'.format(self.campaign.__str__(), self.name)

class Event(models.Model):
    campaign = models.ForeignKey(Campaign)
    session = models.ForeignKey(Session)
    threads = models.ManyToManyField(Thread, blank=True)
    content = models.TextField(blank=True)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} - "{}..."'.format(self.campaign.__str__(), self.content[:50])

