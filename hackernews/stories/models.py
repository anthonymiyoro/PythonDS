from django.db import models

from urlparse import urlparse
from django.contrib.auth.models import User

# Create your models here..

class Story(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()
    points = models.IntegerField()
    poster = models.ForeignKey(User)
    created_at
    updated_at


@property
def domain(self):
   return urlparse(self.url).netloc
