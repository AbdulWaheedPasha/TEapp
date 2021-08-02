from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"