from django.shortcuts import render
from .models import ToDoList, Item


def index(request):
    return render(request, 'base/base.html')