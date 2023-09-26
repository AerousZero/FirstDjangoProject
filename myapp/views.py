from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("<h1> Clueless Django Learner </h1>")

def ahome(request):
    return HttpResponse("<h1>Root </h1>")

def root(request):

    people = [
        {"first":"Jon","last":"Doe","address":"KTM"},
        {"first":"Jon","last":"Doe","address":"KTM"},
        {"first":"Jon","last":"Doe","address":"KTM"},
        {"first":"Jon","last":"Doe","address":"KTM"},
    ]
    student = {"name":"jon", "age":18, "address":"KTM"}

    return render(request, template_name="myapp/home.html", context= {"title": "Root Page","people":people})

