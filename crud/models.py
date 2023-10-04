from django.db import models

# Create your models here.
class ClassRoom(models.Model):
    name = models.CharField(max_length=50)


    def __str__(self):
        return self.name
    
class Student(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    age = models.IntegerField()

    classroom = models.ForeignKey(ClassRoom, on_delete = models.CASCADE, related_name="classroom_students", null=True, blank=True)

    def __str__(self):
        return self.name
    
class StudentProfile(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE) #relatedname=
    profilePic = models.FileField(null=True, blank=True,upload_to="profilePics")
    address = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"Profile of {self.student.name}"