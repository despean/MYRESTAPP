from django.db import models
from simpleapi.tweetcollections import *

# Create your models here.


class Trending(models.Model):
    id = models.IntegerField(primary_key=True)
    text = models.TextField()
    username = models.CharField(max_length=255)
    source = models.TextField()
    screen_name = models.CharField(max_length=255)
    profile_image = models.TextField()



