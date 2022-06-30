from django.http import HttpResponse
from django.shortcuts import render, redirect
from service.models import Service
from service.models import Reg

from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth


def home(request):

    service_data = Service.objects.all()
    # for a in service_data:
        # print(a.username)
        # print(a.Ctitle)
        # print(a.description)
    
    data1={
        'service_data':service_data
        
    }
    if request.method=='POST':
        
        username = request.POST.get('uname')
        Ctitle = request.POST.get('title')
        description = request.POST.get('desc')
        db=Service(username=username,Ctitle=Ctitle,description=description)
        db.save()
        return redirect('home')

        

        # data={
        #     'username':username,
        #     'Ctitle':Ctitle,
        #     'description':description
        # }
        return render(request,"home.html")



    return render(request,"home.html",data1)




# register page
def reg(request):
    if request.method=='POST':
        name = request.POST.get('name')
        username = request.POST.get('user_name')
        password = request.POST.get('password')

        db=Reg(name=name,reg_user_name=username,password=password)
        db.save()
        # messages.success(request,"your account has been successfull create")
        # return redirect('login')
    
    return render(request,"register.html")




        

