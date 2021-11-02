from django.db import models

# Create your models here.

class Room(models.Model):
    #host =
    # #topic = 
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    #participants =
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Profile(models.Model):
    name = models.CharField(max_length=270)
    description = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=270)

    def __str__(self):
        return self.name