from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from .serializers import BucketlistSerializer
from .models import BucketList
from .permissions import IsOwner

# Create your views here.


class CreateView(generics.ListCreateAPIView):
    queryset = BucketList.objects.all()
    serializer_class = BucketlistSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BucketList.objects.all()
    serializer_class = BucketlistSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)
