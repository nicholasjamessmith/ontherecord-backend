from .models import Review
from rest_framework import viewsets, permissions
from .serializers import ReviewSerializer

class ReviewViewSet(viewsets.ModelViewSet):
  # The main query for the index route, queryset is a list of all Review objects
  queryset = Review.objects.all()
  # Serializer class for serializing output, used to to control which serializer class should be used for serializing and deserializing queryset and model instances
  serializer_class = ReviewSerializer
  # Permission class to set permission level (optional)
  permission_classes = [permissions.AllowAny]
  