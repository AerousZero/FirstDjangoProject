from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from .views import hello_world, MessageView, SimpleStudentView, SimpleStudentListView 
from .views import ClassRoomDetailAPIView, ClassRoomAPIView, StudentDetailAPIView, StudentAPIView, StudentProfileAPIView
from .views import ClassRoomListAPIView , ClassRoomCreateAPIView, ClassRoomRetrieveAPIView, ClassRoomUpdateAPIView, ClassRoomDestroyAPIView, ClassRoomListCreateAPIView ,ClassRoomObjectAPIView
from .views import StudentListAPIView , StudentCreateAPIView , StudentRetrieveAPIView, StudentUpdateAPIView, StudentDestroyAPIView, StudentListCreateAPIView, StudentObjectAPIView
from .views import ClassRoomViewSet, ClassRoomListUpdateViewSet, StudentViewSet
from.login import UserLoginView

router = DefaultRouter()
router.register('classroom-viewset', ClassRoomViewSet)
router.register('classroom-list-update', ClassRoomListUpdateViewSet)
router.register('student-viewset', StudentViewSet)



urlpatterns = [
    path('hello-world/', hello_world),
    path('message/', MessageView.as_view()),
    
    path('simple-student/<int:id>/', SimpleStudentView.as_view()),
    path('simple-student-list/', SimpleStudentListView.as_view()),
    path("login/",UserLoginView.as_view, name="login")
]

urls_serializers = [
    path('classroom/<int:id>', ClassRoomDetailAPIView.as_view()),
    path('classroom/', ClassRoomAPIView.as_view()),

    path('student/<int:id>', StudentDetailAPIView.as_view()),
    path('student/', StudentAPIView.as_view()),

    path('student-profile/', StudentProfileAPIView.as_view()),

]

generic_classroom_urls = [
    path("generic-classroom-list/", ClassRoomListAPIView.as_view()),
    path("generic-classroom-create/", ClassRoomCreateAPIView.as_view()),
    
    path("generic-classroom-retreive/<int:pk>/", ClassRoomRetrieveAPIView.as_view()),
    path("generic-classroom-update/<int:pk>/", ClassRoomUpdateAPIView.as_view()),
    path("generic-classroom-destroy/<int:pk>/", ClassRoomDestroyAPIView.as_view()),

    path("generic-classroom/",ClassRoomListCreateAPIView.as_view()),
    path("generic-classroom/<int:pk>/", ClassRoomObjectAPIView.as_view()),

]


generic_student_urls = [
    path("generic-student-list/", StudentListAPIView.as_view()),
    path("generic-student-create/", StudentCreateAPIView.as_view()),
    
    path("generic-student-retreive/<int:pk>/", StudentRetrieveAPIView.as_view()),
    path("generic-student-update/<int:pk>/", StudentUpdateAPIView.as_view()),
    path("generic-student-destroy/<int:pk>/", StudentDestroyAPIView.as_view()),

    path("generic-student/",StudentListCreateAPIView.as_view()),
    path("generic-student/<int:pk>/", StudentObjectAPIView.as_view()),

]

urlpatterns += urls_serializers + generic_classroom_urls + generic_student_urls + router.urls
