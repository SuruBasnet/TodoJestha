from django.shortcuts import render,redirect
from .models import Todo
from .forms import TodoForm

# Create your views here.
def home(request):
    todos = Todo.objects.all()
    return render(request,'index.html',context={'todos':todos})

def create_todo(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        status = request.POST.get('status')

        Todo.objects.create(name=name,description=description,status=status)
    return render(request,'create.html')

def edit_todo(request,pk):
    todo_obj = Todo.objects.get(id=pk)
    form = TodoForm(instance=todo_obj)
    if request.method == 'POST':
        form = TodoForm(instance=todo_obj,data=request.POST)
        if form.is_valid():
            form.save()
    return render(request,'edit.html',context={'form':form})

def delete_todo(request,pk):
    todo_obj = Todo.objects.get(id=pk)
    todo_obj.delete()
    return redirect('home')