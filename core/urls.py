from fcm_django.api.rest_framework import FCMDeviceViewSet

from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()

router.register('devices', FCMDeviceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]