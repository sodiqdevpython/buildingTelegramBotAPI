from django.urls import path
from .views import GetAllData, PostData

urlpatterns = [
    path('', GetAllData.as_view()),
    path('add/', PostData.as_view())
]
