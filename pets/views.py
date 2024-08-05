from django.shortcuts import render

# from django.views.generic import TemplateView, ListView, DetailView
from rest_framework import generics
from .models import Pet
from .serializer import PetSerializer
from .permissions import IsOwnerOrReadOnly


from rest_framework.permissions import AllowAny, IsAuthenticated

class PetList(generics.ListCreateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer 
    permission_classes = [AllowAny]

class PetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = [IsOwnerOrReadOnly]