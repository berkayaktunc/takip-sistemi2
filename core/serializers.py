from rest_framework import serializers
from db.models import LeaveRequest

class LeaveRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveRequest
        fields = ['id', 'user', 'leave_type', 'status', 'created_at', 'updated_at']
