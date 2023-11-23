
from django.http import JsonResponse

from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import ListAPIView , CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet 
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.decorators import action


from crud.models import  ClassRoom, Student, StudentProfile

from .serializers import ClassRoomSerializer , ClassRoomModelSerializer ,StudentModelSerializer, StudentProfileModelSerializer

from .viewsets import ListUpdateViewSet

from .permissions import IsSuperAdminUser

# Create your views here.
def hello_world(request):
    response = {"message":"Hello World"}
    return JsonResponse(response)
 
class MessageView(APIView):
    def get(self, *args, **kwargs):
        return Response([
            {"name" : "Anukul", "address":"LTP", "age":69},
            {"name" : "Bhupendra", "address":"LTP", "age":69},
            {"name" : "Srijan", "address":"LTP", "age":69},
        ])
    
class SimpleStudentView(APIView):
    def get(self, *args, **kwargs):

        try:
            std = Student.objects.get(id=kwargs['id'])
        except Student.DoesNotExist:
            return Response({
                "detail": "Not Found"
            }, status = status.HTTP_404_NOT_FOUND)
        
        return Response({
            "name": std.name,
            "email": std.email, 
            "age": std.age,
            "classroom": std.classroom.name
        })
    

class SimpleStudentListView(APIView):
    def get(self,*args,**kwargs):
        stds = Student.objects.all()
        data = []
        for std in stds:
            data.append({
                
                "name":std.name,
                "email":std.email,
                "age":std.age,
                "classroom":std.classroom.name
            })
        return Response(data)

    def post(self, *args, **kwargs):

        print(self.request.data)

        name = self.request.data.get("name")
        email = self.request.data.get("email")
        age = self.request.data.get("age")
        classroom = self.request.data.get("classroom")

        std = Student.objects.create(name=name, email=email , age=age, classroom_id=classroom)

        return Response({
            "Detail" : " Student has been register! "
        }, status = status.HTTP_201_CREATED)
    

class ClassRoomDetailAPIView(APIView):
    def get(self, *args, **kwargs):
        try:
            csrm = ClassRoom.objects.get(id=kwargs['id'])
        except ClassRoom.DoesNotExist:
            return Response({
                "detail": "Not Found"
            }, status = status.HTTP_404_NOT_FOUND)
        serializer = ClassRoomSerializer(csrm)
        return Response(serializer.data)
        
class ClassRoomAPIView(APIView):
    def post(self, request ,*args, **kwargs):
        serializer = ClassRoomSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            ClassRoom.objects.create(name=name)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, *args, **kwargs):
        csrms = ClassRoom.objects.all()
        serializer = ClassRoomModelSerializer(csrms, many=True)
        return Response(serializer.data)
    

class StudentDetailAPIView(APIView):
    def get(self,*args,**kwargs):
        try:
            std = Student.objects.get(id=kwargs['id'])
        except Student.DoesNotExist:
            return Response ({
                'detail': 'Student Not found'
            },status=status.HTPP_404_NOT_FOUND)
        serializer = StudentModelSerializer(std)
        return Response(serializer.data)
            
class StudentAPIView(APIView):
    def post(self, request ,*args, **kwargs):
        serializer = StudentModelSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get("name")
            email = serializer.data.get("email")
            age = serializer.data.get('age')
            classroom = serializer.data.get('classroom')

            Student.objects.create(name=name,email=email,age=age,classroom_id=classroom)
          
            # serializer.save()
            # print(serializer.data.get("age"))

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, *args, **kwargs):
        stds = Student.objects.all()
        serializer = StudentModelSerializer(stds, many=True , context ={"request": self.request})
        return Response(serializer.data)
    
class StudentProfileAPIView(APIView):
    def get(self, *args, **kwargs):
        sp = StudentProfile.objects.all()
        ser = StudentProfileModelSerializer(sp, many=True, context = {"request": self.request})
        return Response(ser.data)

    def post(self, *args, **kwargs):
        ser = StudentProfileModelSerializer(data=self.request.data)
        ser.is_valid(raise_exception = True)
        ser.save()
        return Response (ser.data, status=status.HTTP_201_CREATED)
        
class ClassRoomListAPIView(ListAPIView):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomModelSerializer


class ClassRoomCreateAPIView(CreateAPIView):
    #queryset = ClassRoom.objects.all() not needed in create
    serializer_class = ClassRoomModelSerializer


class ClassRoomRetrieveAPIView(RetrieveAPIView):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomModelSerializer

class ClassRoomUpdateAPIView(UpdateAPIView):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomModelSerializer

class ClassRoomDestroyAPIView(DestroyAPIView):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomModelSerializer
    
class ClassRoomListCreateAPIView(ListCreateAPIView):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomModelSerializer

class ClassRoomObjectAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomModelSerializer

# For Student
class StudentListAPIView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer


class StudentCreateAPIView(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer


class StudentRetrieveAPIView(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

class StudentUpdateAPIView(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

class StudentDestroyAPIView(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    
class StudentListCreateAPIView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

class StudentObjectAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer


class ClassRoomViewSet(ModelViewSet):
    #pagination_class = LimitOffSetPagination
    #pagination_class = PageNumberPagination
    #permission_classes = [IsAuthenticated, ]
    #permission_classes = [AllowAny, ]
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomModelSerializer

    def get_permission(self):
        if self.request.method == "GET":
            return [AllowAny(), ]
        return [IsSuperAdminUser(), ]
    
    def grt_serializer_class(self):
        if self.action == "student":
            return StudentModelSerializer
        return ClassRoomModelSerializer
    
    @action(detail = True)
    def student(self, *args, **kwargs):
        classroom_obj = self.get_object()
        students = Student.objects.filter(classroom = classroom_obj)
        ser = self.get_serializer(students, many = True)
        return Response(ser.data)        


class ClassRoomListUpdateViewSet(ListUpdateViewSet):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomModelSerializer




class StudentViewSet(ModelViewSet):
    #pagination_class = LimitOffsetPagination
    #pagination_class = PageNumberPagination
    #permission_classes = [IsAuthenticated, ]
    #permission_classes = [AllowAny, ]
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ["name","email"]
    filterset_fileds = ["age","name","classroom__name"]

    def get_queryset(self):
        #classroom = self.request.query_params.get("classroom") works in drf not in django
        classroom = self.request.Get.get("classroom") #works in both
        if classroom:
            return Student.objects.filter(classroom_id=classroom)
        return Student.objects.all
    