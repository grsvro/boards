from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from todo import models


def index(request):
    all = models.Task.objects.all()
    context = {"all_task": all}
    return render(request, "todo/index.html", context)


def create(request):
    new_task = models.Task()
    new_task.date = request.POST.get("date")
    new_task.menu = request.POST.get("menu")
    new_task.weight = request.POST.get("weight")
    new_task.age = request.POST.get("age")
    new_task.save()  # ここでテーブルにデータが保存される
    return HttpResponseRedirect(reverse("todo:index"))


def delete(request, task_id):
    delete_task = models.Task.objects.get(id=task_id)
    delete_task.delete()
    return HttpResponseRedirect(reverse("todo:index"))
