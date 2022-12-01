# from asyncio import all_tasks
# import imp
import imp
from django.shortcuts import redirect, render
from django.http import HttpResponse
from todolist_app.models import Tasklist
from todolist_app.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def todolist(request):
    # return HttpResponse("Welcom to Task page")
    
    # context = {"welcome_text":"Welcome to Todo List App from Jinja2."} #key:value
    # return render(request, 'todolist.html', context)
    if request.method == "POST":
       form = TaskForm(request.POST or None)
       if form.is_valid():
           instance = form.save(commit=False)
           instance.manage = request.user
           instance.save()
           messages.success(request, ('New Task Added!'))
           return redirect(('todolist'))
    else:
        # all_tasks = Tasklist.objects.all
        # return render(request, 'todolist.html', {'all_tasks': all_tasks})
        
        # Paginator:
        all_tasks = Tasklist.objects.filter(manage=request.user)
        paginator = Paginator(all_tasks, 5) # if it's 1 it be 1-5 and if it's 6 it be 6-10
        page = request.GET.get('pg')
        all_tasks = paginator.get_page(page)
        return render(request, 'todolist.html', {'all_tasks': all_tasks})

def abc(request):
    return HttpResponse("Welcome to abc in task path")

def about(request):
    context = {'about_text':"Welcome to About."}
    return render(request, 'about.html', context)

@login_required
def contact(request):
    context = {'contact_text':"Welcome to Contact."}
    return render(request, 'contact.html', context)

@login_required
def delete_task(request, task_id):
    task = Tasklist.objects.get(pk=task_id)
    if task.manage == request.user:
        task.delete()
    else:
        messages.error(request, ("Access Restrited, You Are Not Allowed!"))
    return redirect('todolist')

def edit_task(request, task_id):
    if request.method == "POST":
        task = Tasklist.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance = task) #this selected previous instance
        if form.is_valid():
            form.save()
        messages.success(request, ('New Task Edited!'))
        return redirect(('todolist'))
    else:
        task_obj = Tasklist.objects.get(pk=task_id)
        return render(request, 'edit.html', {'task_obj': task_obj})
 
@login_required   
def complete_task(request, task_id):
    task = Tasklist.objects.get(pk=task_id)
    if task.manage == request.user:
        task.done = True
        task.save()
    else:
        messages.error(request, ("Access Restrited, You Are Not Allowed!"))
    return redirect('todolist')

@login_required
def pending_task(request, task_id):
    task = Tasklist.objects.get(pk=task_id)
    task.done = False
    task.save()
    return redirect('todolist')

def index(request):
    context = {'index_text':"Welcome to Index Page.",}
    return render(request, 'index.html', context)

