from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .models import PrimeNumber
from .serializers import PrimeSerializer
from rest_framework import viewsets

#create view using CreateAPIView 

class PrimeView(CreateAPIView):
    queryset = PrimeNumber.objects.all()
    serializer_class = PrimeSerializer

    