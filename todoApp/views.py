

from django.shortcuts import render
from rest_framework import viewsets
from .models import TodoApp
from .serializers import TodoSerializes


class TodoViewset(viewsets.ModelViewSet):
    queryset = TodoApp.objects.filter()
    serializer_class = TodoSerializes
