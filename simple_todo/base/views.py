from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList


def index(request):
    todo_items = ToDoList.objects.all()
    context = {'page': 'index', 'todo_items': todo_items}
    return render(request, 'base/index.html', context)



def create(request):
    if request.method == 'POST':
        form = CreateNewList(request.POST) # Create a for that has those characters populated
        if form.is_valid():
            n = form.cleaned_data['name']
            t = request.user.todolist_set.create(name=n)
            t.save()
        return HttpResponseRedirect('/%i' %t.id)

    else:
        form = CreateNewList()

    form = CreateNewList()
    context = {'page': 'create', 'form': form}
    return render(request, 'base/create.html', context)

def todo(request, pk):
    todoitem = ToDoList.objects.get(id=pk)
    if todoitem in request.user.todolist.all():

        if request.method == 'POST':
            if request.POST.get('save'):
                for item in todoitem.item_set.all():
                    if request.POST.get('c' + str(item.id)) == 'clicked':
                        item.complete = True
                    else:
                        item.complete = False

                    item.save()

            elif request.POST.get('newItem'):
                txt = request.POST.get('new')
                if len(txt) > 2:
                    todoitem.item_set.create(text=txt, complete=False)
                else:
                    print('Invalid')

        context = {'page': 'index', 'todo_item': todoitem}
        return render(request, 'base/list.html', context)

    else:
        return render(request, 'base/404.html')