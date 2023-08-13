from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create_task", views.create_task, name="create_task"),
    path("task_action", views.task_action, name="task_action"),
    path("update", views.update, name="update_form"),
]