from django.shortcuts import render
from .models import ToDoList, Item
from .forms import CreateNewList


def index(request):
    todo_items = ToDoList.objects.all()
    context = {'page': 'index', 'todo_items': todo_items}
    return render(request, 'base/index.html', context)

def todo(request):
    pass

def create(request):
    form = CreateNewList()
    context = {'page': 'create', 'form': form}
    return render(request, 'base/create.html', context)