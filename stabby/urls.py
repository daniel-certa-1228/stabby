"""
URL configuration for stabby project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from stabby_web import views

app_name = "stabby_web"
urlpatterns = [
    path("", views.index, name="knives"),
    path("sharpeners/", views.sharpeners, name="sharpeners"),
    path("api/get_knife_grid/", views.get_knife_grid, name="get_knife_grid"),
    path("admin/", admin.site.urls),
]
