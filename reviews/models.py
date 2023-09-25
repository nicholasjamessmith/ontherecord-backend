from django.db import models

# Create your models here.
class Review(models.Model):
  image = models.CharField(max_length=100)
  title_of_work = models.CharField(max_length=100)
  artist = models.CharField(max_length=100)
  review = models.CharField(max_length=100)


