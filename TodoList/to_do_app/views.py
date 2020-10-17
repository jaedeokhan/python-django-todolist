from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *
# Create your views here.
def index(request):
    todos = Todo.objects.all()
    content = {'todos' : todos}
    return render(request, "to_do_app/index.html", content)

def createTodo(request):
    user_input_str = request.POST['todoContent']
    new_todo = Todo(content = user_input_str)
    new_todo.save()
    return HttpResponseRedirect(reverse('index'))

def deleteTodo(request):
    deleteNum = request.GET['todoNum']
    todo = Todo.objects.get(id = deleteNum)
    todo.deleteYn = True
    print("삭제한 todo의 id : " + deleteNum)
    todo.save()
    return HttpResponseRedirect(reverse('index'))