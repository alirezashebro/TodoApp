from django.shortcuts import render
from todo.models import *

def index(request):
    context = {}
    tasks = Task.objects.all()
    context.update({'tasks': tasks})
    return render(request, "index.html", context)
