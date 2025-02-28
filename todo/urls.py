from django.urls import path
from . import views

app_name = "todo"

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("delete/<int:task_id>", views.delete, name="delete"),
]
