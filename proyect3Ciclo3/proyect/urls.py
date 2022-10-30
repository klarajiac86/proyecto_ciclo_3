"""proyect URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from .router import router
from appProyect import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

    path('login/', views.PersonaLoginAdminView.as_view()),
    path('personas/', views.PersonaListView.as_view()),
    path('persona/<int:pk>/', views.PersonaSearchView.as_view()),


    path('pacientes/', views.PacienteListView.as_view()),
    path('paciente/', views.PacienteCreateView.as_view()),
    path('paciente/<int:pa_persona>/', views.PacienteSearchView.as_view()),
    path('pacienteDelete/<int:pa_persona>/', views.PacienteDeleteView.as_view()),

    path('medicos/', views.MedicoListView.as_view()),
    path('medico/', views.MedicoCreateView.as_view()),
    path('medicoDelete/<int:me_persona>/', views.MedicoDeleteView.as_view()),
]
