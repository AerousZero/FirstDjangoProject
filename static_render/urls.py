from django.urls import path
from .views import staticHome , Portfolio

urlpatterns = [
   path("",staticHome),
   path('portfolio/',Portfolio), 
]
