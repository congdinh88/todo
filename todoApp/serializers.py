
from dataclasses import field
from pyexpat import model
from rest_framework.serializers import ModelSerializer
from .models import TodoApp


class TodoSerializes (ModelSerializer):
    class Meta:
        model = TodoApp
        fields = ['id', 'name', 'complete']
