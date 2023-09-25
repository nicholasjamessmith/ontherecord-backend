from django.db import models

# Create your models here.
class Review(models.Model):
  image = models.CharField(max_length=1000)
  title_of_work = models.CharField(max_length=1000)
  artist = models.CharField(max_length=1000)
  review = models.CharField(max_length=1000)


