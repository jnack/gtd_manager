from django.shortcuts import render
from .models import Task, Project
from django.utils import timezone

# Create your views here.
def task_list(request):
    tasks = Task.objects.filter(stage = 'prep').order_by('due_date')
    return render(request, 'taskManager/task_list.html', {'tasks': tasks})
