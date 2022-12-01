from email import message
import imp
from django.shortcuts import HttpResponse, redirect, render
from .forms import CustomRegisterForm
from django.contrib import messages

# Create your views here.
def register(request):
    # return HttpResponse("users_app working!")
    
    if request.method == "POST":
        register_form = CustomRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, ("New User Account Created, Login To Get Started!"))
            return redirect('register')
    else:
        register_form = CustomRegisterForm()
    return render(request, 'register.html', {'register_form': register_form})