from django.urls import path
from django.urls.conf import include
from . import views
from rest_framework import routers
from .views import EventViewSet

router = routers.DefaultRouter()
router.register('event',views.EventViewSet)


urlpatterns = [
    # path('', views.getRouter, name="routes"),
    path('',include(router.urls)),
]