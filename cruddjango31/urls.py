"""cruddjango31 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from postres.views import PostresListado, PostreDetalle, PostreCrear, PostreActualizar, PostreEliminar

urlpatterns = [
    path('admin/', admin.site.urls),
 
    # La ruta 'leer' en donde listamos todos los registros o postres de la Base de Datos
    path('postres/', PostresListado.as_view(template_name = "postres/index.html"), name='leer'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un postre o registro 
    path('postres/detalle/<int:pk>', PostreDetalle.as_view(template_name = "postres/detalles.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo postre o registro  
    path('postres/crear', PostreCrear.as_view(template_name = "postres/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un postre o registro de la Base de Datos 
    path('postres/editar/<int:pk>', PostreActualizar.as_view(template_name = "postres/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un postre o registro de la Base de Datos 
    path('postres/eliminar/<int:pk>', PostreEliminar.as_view(), name='eliminar'),    
] 


