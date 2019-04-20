from django.shortcuts import render
from rest_framework import generics
from .serializers import BucketlistSerializer
from .models import BucketList

# Create your views here.


class CreateView(generics.CreateAPIView):
    queryset = BucketList.objects.all()
    serializer_class = BucketlistSerializer

    def perform_create(self, serializer):
        serializer.save()


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BucketList.objects.all()
    serializer_class = BucketlistSerializer
