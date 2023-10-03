from django.shortcuts import render, redirect
from temp_inheritance.models import student
from django.http import HttpRequest, HttpResponse
# Create your views here.

def studentForm(request:HttpRequest):

    #print(request.method)

    #print(request.POST)
    if request.method == "POST":
        name = request.POST.get("Name")
        email = request.POST.get("Email")
        age = request.POST.get("Age")

        student.objects.create(name = name, email = email, age = age)
        return redirect("Students")
    
    return render(request , "tempForms/studentForm.html")