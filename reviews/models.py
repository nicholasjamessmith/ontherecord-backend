from django.db import models

# Create your models here.
class Review(models.Model):
  image = models.CharField(max_length=255)
  title_of_work = models.CharField(max_length=255)
  artist = models.CharField(max_length=255)
  review = models.CharField(max_length=255)


