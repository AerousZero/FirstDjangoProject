
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('inherit/',include('temp_inheritance.urls')),
    path('sr/', include('static_render.urls')),
    path('forms/', include('tempForms.urls')),
]
