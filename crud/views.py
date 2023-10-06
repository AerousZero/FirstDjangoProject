from django.shortcuts import render, redirect
from .models import ClassRoom, Student, StudentProfile
# Create your views here.


def classroom(request):

    if request.method == "POST":
        name = request.POST.get("name")
        ClassRoom.objects.create(name=name)
        return redirect("crud_classroom")

    classrooms = ClassRoom.objects.all()
    return render(request, "crud/classroom.html", {"title": "ClassRoom", "classrooms": classrooms})


def classroom_delete(request, id):
        classroom = ClassRoom.objects.get(id=id)

        if request.method == "POST":
             classroom.delete()
             return redirect('crud_classroom')

        return render(request, 'crud/classroom_delete.html', {"title": "Classroom Delete", "classroom": classroom})


def classroom_update(request, id):
        classroom = ClassRoom.objects.get(id=id)

        if request.method == "POST":
             name = request.POST.get("name")
             ClassRoom.objects.filter(id=id).update(name=name)
             return redirect('crud_classroom')

        return render(request, 'crud/classroom_update.html', {"title": "Classroom Update", "classroom": classroom})


def student(request):
      students = Student.objects.all()
      return render(request, 'crud/student.html', {"title": "Student", "students": students})


def add_student(request):
      if request.method == "POST":
            name = request.POST.get("name")
            email = request.POST.get("email")
            age = request.POST.get("age")
            pp = request.FILES.get('pp')
            address = request.POST.get("address")
            phone = request.POST.get("phone")
            class_id= request.POST.get("classId")

            std = Student.objects.create(
                name=name, email=email, age=age, classroom_id=class_id)
            sp = StudentProfile.objects.create(
                phone=phone, address=address, student=std)
            if pp:
                  sp.profilePic = pp
                  sp.save()

            return redirect("crud_student")
      return render(request, 'crud/add_student.html', {"title": "Add Student","classes":ClassRoom.objects.all()})


def student_detail(request, id):
      print(id)
      std = Student.objects.get(id=id)
      return render(request, 'crud/student_detail.html', {"title": "Detail", "student": std})


def student_update(request, id):
      std = Student.objects.get(id=id)
      if request.method == "POST":
                  name = request.POST.get("name")
                  email = request.POST.get("email")
                  age = request.POST.get("age")
                  address = request.POST.get("address")
                  phone = request.POST.get("phone")
                  pp = request.FILES.get("pp")
                  Student.objects.filter(id=id).update(
                  name=name, email=email, age=age)
                  sp, _ = StudentProfile.objects.update_or_create(
                  student=std, defaults={"address": address, "phone": phone})

                  if pp:
                        sp.profilePic = pp
                        sp.save()
                  return redirect('student_detail', std.id)

      return render(request, 'crud/student_update.html', {"title":"Student Update","student": std})