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

def student(request):
      students = Student.objects.all()
      return render(request, 'crud/student.html', {"title":"Student","students":students} )

def add_student(request):
      if request.method == "POST":
            name = request.POST.get("name")
            email = request.POST.get("email")
            age = request.POST.get("age")
            pp = request.FILES.get('pp')
            address = request.POST.get("address")
            phone = request.POST.get("phone")

            std = Student.objects.create(name=name, email=email, age=age ,classroom_id=3)
            sp = StudentProfile.objects.create(phone=phone, address=address, student=std)

            if pp:
                  sp.profilePic = pp
                  sp.save()

            return redirect ("crud_student")
      return render(request, 'crud/add_student.html', {"title":"Add Student"} )
