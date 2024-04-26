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
    path("knives/detail/<int:knife_id>/", views.knife_detail, name="knife_detail"),
    path("knives/add", views.knife_create, name="knife_create"),
    path("knives/edit/<int:knife_id>/", views.knife_update, name="knife_update"),
    path(
        "sharpeners/detail/<int:sharpener_id>/",
        views.sharpener_detail,
        name="sharpener_detail",
    ),
    path(
        "api/get_blade_grid/<int:knife_id>/",
        views.get_blade_grid,
        name="get_blade_grid",
    ),
    path("api/get_knife_grid/", views.get_knife_grid, name="get_knife_grid"),
    path(
        "api/get_sharpener_grid/", views.get_sharpener_grid, name="get_sharpener_grid"
    ),
    path(
        "api/get_knife_work_log_grid/<int:knife_id>/",
        views.get_knife_work_log_grid,
        name="get_knife_work_log_grid",
    ),
    path(
        "api/get_sharpener_work_log_grid/<int:sharpener_id>/",
        views.get_sharpener_work_log_grid,
        name="get_sharpener_work_log_grid",
    ),
    path("admin/", admin.site.urls),
]
