from django.db.models import query
from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import JsonResponse 
from rest_framework import viewsets
from .models import Event
from .serializers import EventSerializer

# Create your views here.
def getRouter(request):
        return JsonResponse('Hello',safe=False)

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer