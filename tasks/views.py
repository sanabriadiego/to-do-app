from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.shortcuts import get_object_or_404

# Create your views here.
def home(request):
    return render(request, "index.html")

def all_tasks(request):
    tasks = Task.objects.filter(completed=False)
    return render(request, "tasks.html", {
        'tasks': tasks
    })

def completed_tasks(request):
    tasks = Task.objects.filter(completed=True)
    print(tasks)
    return render(request, "completed_tasks.html", {
        'tasks': tasks
    })

def create_task(request):
    if request.method == 'GET':
        return render(request, "create_task.html", {
            'form': TaskForm
        })
    else:
        try:
            form = TaskForm(request.POST)
            form.save()
            return redirect('tasks')
        except ValueError:
            return render(request, "create_task.html", {
            'form': TaskForm,
            'error': 'Please use valid values for the fields'
        })

def task_detail(request, task_id):
    if request.method == 'GET':
        task = get_object_or_404(Task, pk=task_id)
        form = TaskForm(instance=task)
        return render(request, 'task_detail.html', {
            'task': task,
            'form': form
        })
    else:
        try:
            task = get_object_or_404(Task, pk=task_id)
            form = TaskForm(request.POST, instance=task)
            form.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'task_detail.html', {
            'task': task,
            'form': form,
            'error': 'Error updating task'
        })

def complete_task(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, pk=task_id)
        task.completed = True
        task.save()
        return redirect('tasks')
    
def delete_task(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, pk=task_id)
        task.delete()
        return redirect('tasks')
