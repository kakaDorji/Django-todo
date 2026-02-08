from django.shortcuts import render
from todo.models import Task

def home(req):
    task=Task.objects.filter(is_completed=False).order_by('updated_at')
    task_completed=Task.objects.filter(is_completed=True)
    context={
        'task':task,
        'task_completed':task_completed
    }

    return render(req,'home.html',context)
