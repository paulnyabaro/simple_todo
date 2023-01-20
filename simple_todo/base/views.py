from django.shortcuts import render
from .models import ToDoList, Item


def index(request):
    todo_items = ToDoList.objects.all()
    context = {'todo_items': todo_items}
    return render(request, 'base/index.html', context)

def todo(request):
    context = {'todos': todos}