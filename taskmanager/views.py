from django.shortcuts import render, redirect, get_object_or_404
from .models import Task


# Create your views here.
def task_list(request):
    tasks = Task.objects.all().order_by("-createdAt")
    return render(request, "taskmanager/task_list.html", {"tasks": tasks})


def add_task(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        Task.objects.create(title=title, description=description)
        return redirect("task_list")
    return render(request, "taskmanager/add_task.html")


def mark_completed(request, id):
    task = get_object_or_404(Task, id=id)
    task.is_completed = not task.is_completed
    task.save()
    return redirect("task_list")


def delete_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect("task_list")


def edit_task(request, id):
    task = get_object_or_404(Task, id=id)

    if request.method == "POST":
        task.title = request.POST["title"]
        task.description = request.POST["description"]
        task.save()
        return redirect("task_list")

    return render(request, "taskmanager/edit_task.html", {"task": task})
