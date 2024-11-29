import json
from channels.generic.websocket import AsyncWebsocketConsumer

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # WebSocket bağlantısı kurulduğunda yapılacak işlemler
        self.room_group_name = 'notifications'

        # Kanal grubuna katıl
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        # WebSocket bağlantısını kabul et
        await self.accept()

    async def disconnect(self, close_code):
        # WebSocket bağlantısı kapandığında yapılacak işlemler
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Bir mesaj geldiğinde çalışacak fonksiyon
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Gruba mesaj gönder
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'send_message',
                'message': message
            }
        )

    # Gruba gönderilen mesajı al
    async def send_message(self, event):
        message = event['message']

        # WebSocket'e mesaj gönder
        await self.send(text_data=json.dumps({
            'message': message
        }))
