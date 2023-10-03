from django.urls import path
from .views import studentForm

urlpatterns = [
    path('',studentForm,name="studentForm"),
    ]