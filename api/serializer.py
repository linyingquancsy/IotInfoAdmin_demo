'''
创建 序列化器
'''
from rest_framework import serializers
from api.models import Sensor


class SensorSer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'