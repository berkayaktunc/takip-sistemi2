from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from datetime import date, datetime

class CustomUser(AbstractUser):
    annual_leave_days = models.IntegerField(default=15)  # Yeni alan: Yıllık izin
    role = models.CharField(max_length=10, choices=[('personnel', 'Personnel'), ('admin', 'Admin')], default='personnel')

    def __str__(self):
        return self.username

class Attendance(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    check_in = models.TimeField(null=True)
    check_out = models.TimeField(null=True)

    def __str__(self):
        return f"{self.user.username} - {self.date}"

class Leave(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Leave for {self.user.username} from {self.start_date} to {self.end_date}"
    

class LeaveRequest(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(
        max_length=10,
        choices=[('pending', 'Beklemede'), ('approved', 'Onaylı'), ('rejected', 'Reddedildi')],
        default='pending'  # Varsayılan değer "pending"
    )

    def __str__(self):
        return f"Leave Request from {self.user.username}"


class CompanySettings(models.Model):
    start_time = models.TimeField(default='08:00')  # İş başlangıç saati
    end_time = models.TimeField(default='18:00')    # İş bitiş saati
    holidays = models.JSONField(default=list)  # Tatil günleri (örn: ['Cumartesi', 'Pazar'])

    def __str__(self):
        return "Şirket Ayarları"

class Employee(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Burada settings.AUTH_USER_MODEL kullanılıyor
    annual_leave_days = models.FloatField(default=15)
    monthly_work_hours = models.FloatField(default=0)
    is_late = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    

class AttendanceRecord(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='attendance_records')
    date = models.DateField(auto_now_add=True)  # Giriş/çıkış tarihi
    check_in = models.TimeField(null=True, blank=True)  # Giriş saati
    check_out = models.TimeField(null=True, blank=True)  # Çıkış saati

    def calculate_lateness(self):
        # Şirket giriş saatine göre geç kalmayı hesapla
        company_settings = CompanySettings.objects.first()
        if self.check_in and self.check_in > company_settings.start_time:
            lateness = (datetime.combine(date.today(), self.check_in) - 
                        datetime.combine(date.today(), company_settings.start_time)).seconds // 60
            return lateness  # Dakika cinsinden dönüş
        return 0

    def __str__(self):
        return f"{self.employee.user.username} - {self.date}"