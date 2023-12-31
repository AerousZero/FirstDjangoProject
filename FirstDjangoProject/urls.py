from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inherit/',include('temp_inheritance.urls')),
    path('sr/', include('static_render.urls')),
    path('forms/', include('tempForms.urls')),
    path('cb/', include('classbased.urls')),
    path('api/',include('api.urls')),
    path('', include('crud.urls')),
    path('app', include('myapp.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings. MEDIA_URL, document_root=settings.MEDIA_ROOT)
