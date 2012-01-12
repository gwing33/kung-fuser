from django.db import models

# Create your models here.
class Project(models.Model):
  name = models.CharField(max_length=200)
  desc = models.TextField()
  pub_date = models.DateTimeField('date published')
  
  def __unicode__(self):
    return self.name

class UserTest(models.Model):
  USER_TEST_TYPES = (
    ('design', 'Design Review'),
    ('usability', 'Usability Test'),
  )
  
  project = models.ForeignKey(Project)
  name = models.CharField(max_length=200)
  handle = models.SlugField()
  desc = models.TextField()
  url = models.URLField()
  test_type = models.CharField(max_length=1, choices=USER_TEST_TYPES)
  is_private = models.BooleanField(default=False)
  
  def __unicode__(self):
    return self.name

class Task(models.Model):
  user_test = models.ForeignKey(UserTest)
  url = models.TextField()
  task = models.CharField(max_length=400)
  
  def __unicode__(self):
    return self.user_test