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
from django.urls import include, path
from stabby_web import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "stabby_web"
urlpatterns = [
    path("", views.index, name="index"),
    path("knives", views.knives, name="knives"),
    path("knives/detail/<int:knife_id>/", views.knife_detail, name="knife_detail"),
    path("knives/add", views.knife_create, name="knife_create"),
    path("knives/edit/<int:knife_id>/", views.knife_update, name="knife_update"),
    path(
        "knives/detail/<int:knife_id>/blades/add/",
        views.blade_create,
        name="blade_create",
    ),
    path(
        "knives/detail/<int:knife_id>/blades/edit/<int:blade_id>/",
        views.blade_update,
        name="blade_update",
    ),
    path(
        "knives/detail/<int:related_entity_id>/work-logs/add",
        views.work_log_create,
        name="work_log_create",
    ),
    path(
        "knives/detail/<int:related_entity_id>/work-logs/edit/<int:work_log_id>/",
        views.work_log_update,
        name="work_log_update",
    ),
    path(
        "sharpeners/detail/<int:related_entity_id>/work-logs/add",
        views.work_log_create,
        name="work_log_create_sh",
    ),
    path(
        "sharpeners/detail/<int:related_entity_id>/work-logs/edit/<int:work_log_id>/",
        views.work_log_update,
        name="work_log_update_sh",
    ),
    path(
        "knives/detail/<int:related_entity_id>/photos/add",
        views.photo_create,
        name="photo_create",
    ),
    path(
        "knives/detail/<int:related_entity_id>/photos/edit/<int:photo_id>/",
        views.photo_update,
        name="photo_update",
    ),
    path(
        "sharpeners/detail/<int:related_entity_id>/photos/add",
        views.photo_create,
        name="photo_create_sh",
    ),
    path(
        "sharpeners/detail/<int:related_entity_id>/photos/edit/<int:photo_id>/",
        views.photo_update,
        name="photo_update_sh",
    ),
    path("sharpeners/", views.sharpeners, name="sharpeners"),
    path("sharpeners/add", views.sharpener_create, name="sharpener_create"),
    path(
        "sharpeners/edit/<int:sharpener_id>/",
        views.sharpener_update,
        name="sharpener_update",
    ),
    path(
        "sharpeners/detail/<int:sharpener_id>/",
        views.sharpener_detail,
        name="sharpener_detail",
    ),
    path("library/", views.library, name="library"),
    path("library/add", views.photo_create, name="library_item_create"),
    path(
        "api/copy_knife/<int:knife_id>/",
        views.copy_knife,
        name="copy_knife",
    ),
    path(
        "api/delete_blade/<int:blade_id>/",
        views.blade_delete,
        name="blade_delete",
    ),
    path(
        "api/delete_knife/<int:knife_id>/",
        views.knife_delete,
        name="knife_delete",
    ),
    path(
        "api/delete_sharpener/<int:sharpener_id>/",
        views.sharpener_delete,
        name="sharpener_delete",
    ),
    path(
        "api/delete_work_log/<int:work_log_id>/",
        views.work_log_delete,
        name="work_log_delete",
    ),
    path(
        "api/delete_photo/<int:photo_id>/",
        views.photo_delete,
        name="photo_delete",
    ),
    path(
        "api/get_blade_grid/<int:knife_id>/",
        views.get_blade_grid,
        name="get_blade_grid",
    ),
    path(
        "api/get_deployment_type_chart_data/",
        views.get_deployment_type_chart_data,
        name="get_deployment_type_chart_data",
    ),
    path(
        "api/get_lock_type_chart_data/",
        views.get_lock_type_chart_data,
        name="get_lock_type_chart_data",
    ),
    path(
        "api/get_steel_type_chart_data/",
        views.get_steel_type_chart_data,
        name="get_steel_type_chart_data",
    ),
    path(
        "api/get_usa_new_vintage_chart_data/",
        views.get_usa_new_vintage_chart_data,
        name="get_usa_new_vintage_chart_data",
    ),
    path(
        "api/get_country_chart_data/",
        views.get_country_chart_data,
        name="get_country_chart_data",
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
    path(
        "api/set_last_purchase_date/",
        views.set_last_purchase_date,
        name="set_last_purchase_date",
    ),
    path("accounts/login/", views.custom_login_view.as_view(), name="login"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
