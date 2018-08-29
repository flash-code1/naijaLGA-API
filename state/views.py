from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import State, LGA

from .serializers import StateSerializer, StateLGASerializer

# Create your views here.


class StateViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing the states.
    """
    queryset = State.objects.all()
    serializer_class = StateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'state'
    search_fields = ('state')


class StateLGAViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing the states and localgovernment.
    """
    queryset = State.objects.all()
    serializer_class = StateLGASerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'state'
    search_fields = ('state')
