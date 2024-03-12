# notifications/serializers.py
from rest_framework import serializers
from .models import ExpoPushToken

class ExpoPushTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpoPushToken
        fields = ['id', 'user', 'token']
