
from django.contrib import admin
from django.urls import path, include
from usuarios.views import RoleRedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [ 
     path('', include('core.urls')), 
    path('usuarios/', include('usuarios.urls')),  
    path('crud/', include('crud.urls')), 
    path('redirect/', RoleRedirectView.as_view(), name='role_redirect'),
    path('admin/', admin.site.urls),      # Rutas para la app crud
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)