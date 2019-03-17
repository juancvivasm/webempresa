"""webempresa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# Esto va a importar de nuestro fichero core las vistas basicas
from django.urls import include, path

# Extendiendo las funciones en modo de depuracion y ver static - media
from django.conf import settings

urlpatterns = [
    # Paths del core
    path('', include('core.urls')),
    # Paths del Contact
    path('contact/', include('contact.urls')),
    # Paths de Services
    path('services/', include('services.urls')),
    # Paths de Services
    path('blog/', include('blog.urls')),
    # Paths de Pages
    path('page/', include('pages.urls')),
    # Paths del admin
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    # Para ver los archivos estaticos
    from django.conf.urls.static import static

    # Se agrega las direcciones para visualizar
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
