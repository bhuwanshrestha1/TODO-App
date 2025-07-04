from django.urls import path
from . import views

urlpatterns = [
    path("", views.task_list, name="task_list"),
    path("add/", views.add_task, name="add_task"),
    path("complete/<int:id>", views.mark_completed, name="mark_completed"),
    path("delete/<int:id>", views.delete_task, name="delete_task"),
    path("edit/<int:id>/", views.edit_task, name="edit_task"),
]
