from django.urls import path
from .views import student1 , model_student ,profile, Classroom


urlpatterns = [
    path('student/',model_student,name="Students"),
    path('profile/',profile,name="profile"),
    path('profile/',Classroom,name="classroom"),
    path("",student1,name="Inheritt"),
    
]