
from django.http import JsonResponse
from crud.models import Student
from rest_framework.views import APIView
from rest_framework.response import Response

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
            })
        
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

    