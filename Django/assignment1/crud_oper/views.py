from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import UserRegistrationdb
from .forms import userForm, optionForm, updateForm
from django.contrib import messages
# Create your views here.

def registration(request):
    form = userForm()
    if request.method == 'POST':
        form = userForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,'User Registred')    
        else:
            messages.info(request,'Error occured')
        return redirect('/')
    return render(request,'registration.html/',{'form': form})

def showDetails(request):
    users = UserRegistrationdb.objects.all()
    print(users)
    return render(request,'UserDetails.html/',{'users':users})


def option(request):
    form = optionForm()
    if request.method == 'POST':
        form = optionForm(request.POST)
        user_id = request.POST.get('userid')
        print(user_id)
        if UserRegistrationdb.objects.filter(userid = user_id).exists():
            UserRegistrationdb.objects.filter(userid = user_id).delete()
            messages.info(request,'User Deleted')    
        else:
            messages.info(request,'Error occured')
        return redirect('/option')
    return render(request,'option.html/',{'form': form})


def update(request):
    form = userForm()
    if request.method == 'POST':
        user_id = request.POST.get('userid')
        user = UserRegistrationdb.objects.get(userid=user_id)
        form = userForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.info(request,'User Updated')    
        else:
            messages.info(request,'User Not updated')
        return redirect('/')

    return render(request,'update.html/',{'form': form})


def delete(request):
    return render(request,'delete.html/')