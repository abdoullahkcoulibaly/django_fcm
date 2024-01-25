
from firebase_admin.messaging import Message,Notification
# Create your views here.
# views.py

from rest_framework import generics, status
from rest_framework.response import Response
from fcm_django.models import FCMDevice
from .models import Blog
from . serializers import BlogSerializer

class CreateBlogAPI(generics.CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer  # Assurez-vous d'avoir un serializer pour le modèle Blog

    def perform_create(self, serializer):
        # Enregistrez le blog
        blog = serializer.save()

        # Envoyez une notification push à tous les appareils
        devices = FCMDevice.objects.all()
        for d in devices:
            d.send_message(Message(notification=Notification(title="Nouveau Blog", body="Un nouveau blog a été créé!")))

