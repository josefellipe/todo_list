from django.shortcuts import render, redirect
from .forms import TaskForm, UpdateTaskForm
from .models import Task

def tasks(request):
    tasks = Task.objects.all().order_by('-created_at')

    for task in tasks:
        if task.completed == True:
            word = task.description
            new_word = ''
            for letter in word:
                new_word += letter + '\u0336'
            task.description = new_word

    form = TaskForm()
    update_form = UpdateTaskForm()

    context = {
        'form': form,
        'update_form': update_form,
        'tasks': tasks
    }

    return render(request, 'tasks.html', context)


def addTask(request):

    description = request.POST['description']
    Task.objects.create(
        description=description
    )

    return redirect('/tasks')


def deleteTask(request, pk):

    task = Task.objects.get(pk=pk)
    task.delete()

    return redirect('/tasks')


def updateTask(request, pk):

    task = Task.objects.get(pk=pk)
    task.description = request.POST["description"]
    task.save()

    return redirect('/tasks')


def updateStatusTask(request, pk):

    task = Task.objects.get(pk=pk)
    if task.completed == True:
        task.completed = False
    else:
        task.completed = True

    task.save()

    return redirect('/tasks')