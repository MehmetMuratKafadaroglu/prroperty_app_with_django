from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account is created!')
            return redirect('/')
        
    else:
            form = RegisterForm()   
    return render(request,'user/register.html', {'form':form})
