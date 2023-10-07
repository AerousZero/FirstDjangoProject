from django.urls import path
from .views import classroom, classroom_delete, classroom_update, student, add_student, student_detail, student_update, student_delete

urlpatterns = [
    path("student/",student,name="crud_student"),

    path("add-student/",add_student,name="add_student"),
    path("student/detail/<int:id>",student_detail,name="student_detail"),

    path('student/update/<int:id>/',student_update, name='student_update'),
    path('student/delete/<int:id>/',student_delete, name='student_delete'),

    path('class/delete/<int:id>/',classroom_delete, name='classroom_delete'),
    path('class/update/<int:id>/',classroom_update, name='classroom_update'),
    path("",classroom,name="crud_classroom"),
]
