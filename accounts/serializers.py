from rest_framework import serializers
from .models import RoleModel

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleModel
        fields = '__all__'