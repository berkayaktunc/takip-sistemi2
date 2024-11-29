from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Attendance
from datetime import time

def check_tardiness(attendance):
    work_start_time = time(8, 0)  # 08:00 AM
    if attendance.check_in and attendance.check_in > work_start_time:
        tardiness = (attendance.check_in.hour - 8) * 60 + (attendance.check_in.minute)
        # Burada tardiness'i kaydedebilir veya bildirim gönderebilirsiniz
        return tardiness
    # Geç kalma yok
    return 0

@receiver(post_save, sender=Attendance)
def handle_tardiness(sender, instance, **kwargs):
    tardiness = check_tardiness(instance)
    if tardiness > 0:
        # Bildirim logic buraya eklenebilir
        print(f"{instance.user.username} geç kaldı: {tardiness} dakika")

