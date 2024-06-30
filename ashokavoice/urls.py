"""
URL configuration for ashokavoice project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from usuario.views import CreateUsuario, EditUsuario, LoginView, LoginAuth, CambiarPassword
from logro.views import LogroCreateView, EditLogro, RandomLogro, OcultarLogro


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('login/', LoginView.as_view(), name='Login'),
    path('profile/', LoginAuth.as_view(), name='Profile'),
    
    path('put/', CreateUsuario.as_view(), name='CreateUsuario'),
    path('put/<int:usuario_id>', EditUsuario.as_view(), name='UpdateUsuario'),
    path('delete/<int:usuario_id>', EditUsuario.as_view(), name='DeleteUsuario'),
    path('password/', CambiarPassword.as_view(), name='CambiarPassword'),
    
    path('post/logro/', LogroCreateView.as_view(), name='CreateLogro'),
    path('put/logro/<int:logro_id>', EditLogro.as_view(), name='UpdateLogro'),
    path('delete/logro/<int:logro_id>', EditLogro.as_view(), name='DeleteLogro'),
    path('get/logro/', EditLogro.as_view(), name='ListarLogro'),
    path('get/logros/', RandomLogro.as_view(), name='ListarFeedLogro'),
    path('put/ocultar/logro/<int:logro_id>', OcultarLogro.as_view(), name='OcultarLogro'),


]
