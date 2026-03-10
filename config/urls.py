"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.shortcuts import render # Importamos o render para usar arquivos HTML

# Função que carrega a sua página inicial (Home)
def home(request):
    return render(request, 'home.html')

# Função que carregará o seu Quiz
def quiz(request):
    return render(request, 'quiz.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),      # Página inicial: http://127.0.0.1:8000/
    path('quiz/', quiz, name='quiz'), # Página do Quiz: http://127.0.0.1:8000/quiz/
]
