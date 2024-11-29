from django.shortcuts import render
from django.http import JsonResponse
from .models import Notification
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

def send_notification(request):
    # Bir bildirim oluştur
    notification = Notification.objects.create(
        user=request.user,
        message="Yeni bir bildirim var!"
    )

    # Bildirimi WebSocket üzerinden gönder
    channel_layer = get_channel_layer()
    group_name = f"user_{request.user.id}_notifications"

    # Bildirim mesajını kanala gönder
    async_to_sync(channel_layer.group_send)(
        group_name,
        {
            'type': 'send_notification',
            'message': notification.message
        }
    )

    return JsonResponse({"status": "Bildirim gönderildi!"})
