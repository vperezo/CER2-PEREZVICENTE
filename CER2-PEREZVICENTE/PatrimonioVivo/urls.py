"""
URL configuration for PatrimonioVivo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from core import views
from django.contrib.auth import views as auth_views
from core.forms import LoginForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('lugar/<int:id>/', views.detalle, name='detalle'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('gestion/', views.gestion, name='gestion'),
    path('gestion/agregar/', views.agregar, name='agregar'),
    path('gestion/editar/<int:id>/', views.editar, name='editar'),
]
