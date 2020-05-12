from django.db import models
from django.contrib.auth.models import User


class Influencer(models.Model):
    username = models.CharField(max_length=256, unique=True)
    name = models.CharField(max_length=256)
    url_profile_picture = models.URLField(max_length=512)
    bio = models.CharField(max_length=514)
    followers = models.IntegerField()
    posts = models.IntegerField()
    engagement = models.FloatField()
    category = models.CharField(max_length=256)
