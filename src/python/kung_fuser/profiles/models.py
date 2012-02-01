from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
  user = models.ForeignKey(User, unique=True)
  handle = models.SlugField()
  birthday = models.DateTimeField()
  location = models.CharField(max_length=200)
  is_designer = models.BooleanField(default=0)
  is_developer = models.BooleanField(default=0)