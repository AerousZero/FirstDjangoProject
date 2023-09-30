from django.shortcuts import render

# Create your views here.

def staticHome(request):
    return render(request, 'static_render/staticHome.html', {'title':'Static'})

def Portfolio(request):
    return render(request, 'static_render/index.html', {'title':'Portfolio'})