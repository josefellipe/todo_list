from django.shortcuts import render, HttpResponse
from .forms import TaskForm
from .models import Task

def tasks(request):
    tasks = Task.objects.all()
    print(tasks)

    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        print(form.data['description'])

    context = {
        'form': form,
        'tasks': tasks
    }

    return render(request, 'tasks.html', context)
