from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.core.exceptions import ValidationError 
from .models import *
from .forms import *

from django.contrib.auth import authenticate,logout,login
from django.contrib import messages

# Create your views here.

def task(request):
    fm=TaskForm()
    if request.user.is_authenticated:
        task=Task.objects.filter(name=request.user)
        count=Task.objects.filter(name=request.user,complete=False).count()
    
        if request.method=="POST":
           fm=TaskForm(request.POST)
           
           if fm.is_valid():
               title=fm.cleaned_data['title']
               complete=fm.cleaned_data['complete']
          
               reg=Task(name=request.user,title=title,complete=complete)
               
               
               reg.save()
               return redirect('/')
        else:
            fm=TaskForm()
            context={
               'task':task,
               'form':fm,
               'count':count,
               
            }
            return render(request,'app/tasks.html',context)
    else:    
        if request.method=="POST":
           fm=TaskForm(request.POST)
           messages.success(request,'Please login to add tasks!!')
           return HttpResponseRedirect('/')
            
    return render(request,'app/tasks.html',{'form':fm})

def updatetask(request,slug):
   if request.user.is_authenticated: 
        task=Task.objects.get(slug=slug)
        if request.method=="POST":
            fm=TaskForm(request.POST,instance=task)
            if fm.is_valid():
               task.name=request.user    
               task=Task.objects.filter(slug=slug).update(name=request.user,title=fm.cleaned_data['title'],complete=fm.cleaned_data['complete'])   
               print(task)
               fm.save()                
               return HttpResponseRedirect('/')
        else:
            fm=TaskForm(instance=task)
            return render(request,'app/update.html',{'form':fm})


def deletetask(request,slug):
    if request.user.is_authenticated:
        task=Task.objects.get(slug=slug)
        if request.method =="POST":
            task.delete()
            return HttpResponseRedirect('/')
        return render(request,'app/deleteconfirm.html',{'task':task})
    return HttpResponseRedirect('/login/')


def signupform(request):
    fm=UserRegisterationForm()
    if request.method=="POST":
        fm=UserRegisterationForm(request.POST)
       
        if fm.is_valid():
            messages.success(request,'Account Created Successfully.....')
            fm.save()
           
            return redirect('/')
        else:
            return render(request,'app/userregisteration.html',{'form':fm})
    return render(request,'app/userregisteration.html',{'form':fm})


def userlogin(request):
        if not request.user.is_authenticated:
            fm=UserAuthenticationForm()
            if request.method =="POST":
                fm=UserAuthenticationForm(request=request,data=request.POST)
                if fm.is_valid():
                  usname=fm.cleaned_data['username']
                  upass=fm.cleaned_data['password']
                  user=authenticate(username=usname, password=upass)
                  if user is not None:
                    login(request, user)
                    messages.success(request,'Logged in Successfullly!!!!')   
                    return HttpResponseRedirect('/')
            return render(request,'app/login.html',{'form':fm})
        
    
def userlogout(request):
    logout(request)
    return HttpResponseRedirect('/')