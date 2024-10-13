from django.shortcuts import render, redirect
from .models import Task

def tasklist(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/tasklist.html', {'tasks': tasks})

def addtask(request):
    if request.method == 'POST':
        name = request.POST['name']
        Task.objects.create(name=name)
        return redirect('tasklist')
    return render(request, 'tasks/form.html')

def deletetask(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('tasklist')
    return render(request, 'tasks/taskconfirmdelete.html', {'task': task})