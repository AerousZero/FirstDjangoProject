from django.shortcuts import render
from .models import student ,StudentProfile , ClassRoom
# Create your views here.

def Classroom(request):
    classrooms = ClassRoom.objects.all()
    return render(request, template_name="temp_inheritance/model_classroom.html", context={"classroom":classrooms})

def student1(request):
    student1 = [
        {"name":"Srijan","age":21, "address":"KTM"},
        {"name":"Bhups","age":20, "address":"KTM"},
        {"name":"Kools","age":20, "address":"KTM"},
    ]
    return render(request, template_name="temp_inheritance/student.html", context={"student1":student1})

def model_student(request):
    students = student.objects.all()
    return render(request, template_name="temp_inheritance/model_student.html", context={"student":students})


def profile(request):
    sps = StudentProfile.objects.all()
    return render(request, template_name="temp_inheritance/profile.html", context={"profile":sps})


