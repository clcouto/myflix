from django.shortcuts import render
from rest_framework import generics
from actors.models import Actor
from actors.serializers import ActorSerializer

# Create your views here.

class ActorCreateListView(generics.ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

class ActorRetrieveUpdadeDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
