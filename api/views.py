from rest_framework.generics import ListAPIView, CreateAPIView
from .models import MainData
from .serializer import GetSerialData

class GetAllData(ListAPIView):
    queryset = MainData.objects.all()
    serializer_class = GetSerialData

class PostData(CreateAPIView):
    queryset = MainData.objects.all()
    serializer_class = GetSerialData