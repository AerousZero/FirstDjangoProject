from django.db import models

# Create your models here.
class ClassRoom(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class student(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    age = models.IntegerField()

    classroom = models.ForeignKey(ClassRoom, on_delete = models.CASCADE, related_name="classroom_students", null=True, blank=True)

    def __str__(self):
        return self.name #+"##"+ self.email
    


class StudentProfile(models.Model):
    student = models.OneToOneField(student, on_delete=models.CASCADE) #relatedname=
    roll = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)