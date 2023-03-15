from django.conf.urls import url
from django.urls import path

from multi_forms import views

app_name = "multi_forms"

urlpatterns = [
    # url(r'^create/$', views.create, name="create"),
    # url(r'^list/$', views.list, name="list"),
    path("create/", views.create, name="create"),
    path("edit/<id>/", views.edit, name="edit"),
    path("list/", views.list, name="list")
]