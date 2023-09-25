from .models import Review
# from django.contrib.auth.models import User, Group
from rest_framework import serializers

# ReviewSerializer
class ReviewSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    # The model it will serialize
    model = Review
    # The fields that should be included in the serialized output
    fields = ['id', 'image', 'title_of_work', 'artist', 'review']