from django.contrib import admin
from .models import CompanySettings, Employee, AttendanceRecord, LeaveRequest, Attendance
from .models import CustomUser, Employee

admin.site.register(CompanySettings)
admin.site.register(Employee)
admin.site.register(AttendanceRecord)
admin.site.register(LeaveRequest)
admin.site.register(Attendance)

admin.site.unregister(Employee)

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_superuser')

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user', 'annual_leave_days', 'monthly_work_hours', 'is_late')
    list_filter = ('is_late',)