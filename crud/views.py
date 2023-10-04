from django.shortcuts import render, redirect
from .models import ClassRoom, Student, StudentProfile
# Create your views here.


def classroom(request):

    if request.method == "POST":
        name = request.POST.get("name")
        ClassRoom.objects.create(name = name)
        return redirect("crud_classroom")
    
    classrooms = ClassRoom.objects.all()
    return render(request,"crud/classroom.html",{"title":"ClassRoom","classrooms":classrooms})


def classroom_delete(request, id):
        classroom = ClassRoom.objects.get(id=id)

        if request.method=="POST":
             classroom.delete()
             return redirect('crud_classroom')
           
        return render(request, 'crud/classroom_delete.html', {"title":"Classroom Delete","classroom":classroom})

def classroom_update(request, id):
        classroom = ClassRoom.objects.get(id=id)
        
        if request.method=="POST":
             name = request.POST.get("name")
             ClassRoom.objects.filter(id=id).update(name = name)
             return redirect('crud_classroom')

        return render(request, 'crud/classroom_update.html', {"title":"Classroom Update","classroom":classroom})