from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.urls import reverse
from .models import User
# Create your views here.


def home(request):

    if request.method == "POST":
        form=RegistrationForm(request.POST)
        print(request.POST)
        if form.is_valid():
            print(form.cleaned_data['username'])
            print(form.cleaned_data['email'])
            print(form.cleaned_data['password'])
            form.save()
            return redirect('home')

    else:
        form=RegistrationForm()

    user=User.objects.all()
    return render(request,'enroll/add_and_show.html',{'fm':form,'stu_data':user})


def delete_user(request,id):

    if request.method == "POST":
        user=User.objects.get(pk=id)
        user.delete()

    form=RegistrationForm()
    user=User.objects.all()
    return render(request,'enroll/add_and_show.html',{'fm':form,'stu_data':user})


def update_user(request,id):
     
    user=User.objects.get(pk=id)
    if request.method == "POST":
        form=RegistrationForm(request.POST,instance=user)
        
        if form.is_valid():
            form.save()
            return redirect('home')
    
    form=RegistrationForm(instance=user)
    return render(request,'enroll/update_user.html',{'fm':form,'id':id})