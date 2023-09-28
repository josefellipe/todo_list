from django.shortcuts import render, HttpResponse

def tasks(request):
    context = {'tasks': request}
    return render(request, 'tasks.html', context)
