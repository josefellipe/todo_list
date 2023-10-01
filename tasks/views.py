from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task

def tasks(request):
    tasks = Task.objects.all().order_by('-created_at')

    form = TaskForm()

    context = {
        'form': form,
        'tasks': tasks
    }

    return render(request, 'tasks.html', context)


def addTask(request):

    description = request.POST['description']
    Task.objects.create(
        description=description
    )

    return redirect('/tasks')


def deleteTask(request):

    if request.method == 'POST':
        id = request.POST
        print(id)

    return redirect('/tasks')