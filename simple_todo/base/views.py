from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList


def index(request):
    todo_items = ToDoList.objects.all()
    context = {'page': 'index', 'todo_items': todo_items}
    return render(request, 'base/index.html', context)

def todo(request, pk):
    todo_item = ToDoList.objects.get(id=pk)
    context = {'page': 'index', 'todo_item': todo_item}
    return render(request, 'base/list.html', context)

def create(request):
    if request.method == 'POST':
        form = CreateNewList(request.POST) # Create a for that has those characters populated
        if form.is_valid():
            n = form.cleaned_data['name']
            t = ToDoList(name=n)
            t.save()
        return HttpResponseRedirect('/%i' %t.id)

    else:
        form = CreateNewList(   )

    form = CreateNewList()
    context = {'page': 'create', 'form': form}
    return render(request, 'base/create.html', context)