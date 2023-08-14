from django.shortcuts import render, redirect, HttpResponse
from .models import ToDo
from .forms import TodoForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def todo_list(request):
    todos = ToDo.objects.order_by('-date')
    return render(request, 'todoList/todo.html', {'todos': todos})


@login_required
def user_todo_list(request, username):
    user = get_object_or_404(User, username=username)
    todos = ToDo.objects.filter(author_id=request.user.id).order_by('-date')
    return render(request, 'todoList/todo.html', {'todos': todos, 'user': user})


@login_required
def add_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            todo = form.save(commit=False)
            if "done" not in form.cleaned_data:
                todo.done = False
            todo.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'todoList/add_todo.html', {'form': form})


@login_required
def update_todo(request, id):
    todo = get_object_or_404(ToDo, id=id)
    if todo.author == request.user:
        if request.method == "POST":
            form = TodoForm(request.POST, instance=todo)
            if form.is_valid():
                form.save()
                return redirect('todo_list')
        else:
            form = TodoForm(instance=todo)
            return render(request, 'todoList/update_todo.html', {'form': form})
    else:
        return HttpResponse("Forbidden")


@login_required
def delete_todo(request, id):
    todo = get_object_or_404(ToDo, id=id)
    if todo.author == request.user:
        if request.method == 'POST':
            todo.delete()
            return redirect('todo_list')

        return render(request, 'todoList/delete_todo.html', {'todo': todo})
    else:
        return HttpResponse("Forbidden")
