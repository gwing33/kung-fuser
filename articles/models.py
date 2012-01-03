from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
  name = models.CharField(max_length=200)
  handle = models.SlugField()
  content = models.TextField()
  pub_date = models.DateTimeField('date published')
  user = models.ForeignKey(User)
  
  def __unicode__(self):
    return self.name