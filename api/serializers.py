from rest_framework import serializers
from crud.models import ClassRoom, Student, StudentProfile

class ClassRoomSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)

class ClassRoomModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = ['id','name']

class StudentModelSerializer(serializers.ModelSerializer):
    #classroom = ClassRoomModelSerializer() #Get gives you classroom deatail in dectionary but POST expects id 
    class Meta:
        model = Student
        fields = "__all__"  #"__all__" for all fields

    def get_fields(self):
        fields = super().get_fields()
        print(fields)
        request = self.context.get("request")
        if request and request.method == "GET":
            fields['classroom'] = ClassRoomModelSerializer()
        print(fields)
        return fields
    
class StudentProfileModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = ["student","profilePic","address","phone"]

    def get_fields(self):
        fields = super().get_fields()
        print(fields)
        request = self.context.get("request")
        if request and request.method == "GET":
            fields['student'] = StudentModelSerializer()
        print(fields)
        return fields

    

    