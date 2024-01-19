from rest_framework import serializers
from .models import MainData

class GetSerialData(serializers.ModelSerializer):
    class Meta:
        model = MainData
        fields = '__all__'