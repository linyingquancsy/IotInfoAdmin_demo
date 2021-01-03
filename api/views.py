'''
创建 视图聚合
'''
from rest_framework import viewsets
from api.serializer import SensorSer
from api.models import Sensor

class SenViewSet(viewsets.ModelViewSet):
    serializer_class = SensorSer
    queryset = Sensor.objects.all()

