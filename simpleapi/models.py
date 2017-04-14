# -*- coding: utf-8 -*-
from django.db import models
from simpleapi.tweetcollections import *

# Create your models here.


class Trending(models.Model):
    tweet_id = models.BigIntegerField()
    text = models.TextField()
    username = models.TextField()
    source = models.TextField()
    screen_name = models.CharField(max_length=255)
    profile_image = models.TextField()
    hash_tag = models.CharField(max_length=255)



