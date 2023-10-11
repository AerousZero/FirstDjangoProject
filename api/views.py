
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from crud.models import Student, ClassRoom

from .serializers import ClassRoomSerializer , ClassRoomModelSerializer ,StudentModelSerializer

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
        serializer = StudentModelSerializer(stds, many=True)
        return Response(serializer.data)