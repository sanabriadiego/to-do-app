from django.shortcuts import render
from .models import Task

# Create your views here.
def home(request):
    return render(request, "index.html")

def all_tasks(request):
    tasks = Task.objects.all()
    return render(request, "tasks.html", {
        'tasks': tasks
    })

def completed_tasks(request):
    tasks = Task.objects.filter(important=True)
    print(tasks)
    return render(request, "completed_tasks.html", {
        'tasks': tasks
    })