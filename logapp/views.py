from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import user_master
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        address = request.POST['address']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if(password!=cpassword):
            messages.error(request, "Password and Confirm Password feilds must be same!")
            return HttpResponse('Password and Confirm Password feilds must be same!')
        myuser = User.objects.create_user(username, email, password)
        myuser.save()
        myuser1 = user_master(user = myuser, username = username, email = email, address = address, password = password)
        myuser1.save()
        messages.success(request, "Your account has been successfully created")
        return render(request, 'home.html')
    else:
        return HttpResponse('Error 404 - Not Found')


def login(request):
    if request.method=='POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            obj = User.objects.get(email = email)
            obj1 = user_master.objects.get(email = email)
            username = obj1.username
            user = auth.authenticate(username=username, password=password)
            user_obj = User.objects.get(username=username)
            if user is not None:
                auth.login(request, user)
                return redirect('details')
            else:
               messages.info('Invalid Credentials')
               return redirect('login')
        except:
            messages.error(request, 'Invalid Credentials')
            print('Invalid')
            return render(request, 'home.html')
    return render(request, 'home.html')    

def logout(request):
    current_user = request.user
    auth.logout(request)
    return redirect('/')

def details(request):
    users = user_master.objects.all()
    return render(request, 'details.html', {'users': users})

def edit_user(request, user_id):
    obj = User.objects.get(id = user_id)
    obj1 = user_master.objects.get(user = obj)
    if request.method == "POST":
        obj.username = request.POST['username']
        obj.email = request.POST['email']
        obj1.username = request.POST['username']
        obj1.email = request.POST['email']
        obj1.address = request.POST['address']
        obj.save()
        obj1.save()
        return redirect('details')
    return render(request, 'edit.html', {'obj': obj1})


@api_view(['DELETE'])
def delete_user(request, user_id):
    if request.method == "DELETE":
        user = request.user
        user2 = User.objects.get(id = user_id)
        user1 = user_master.objects.get(user = user2)
        user1.delete()
        user2.delete()
        return Response({'msg': "User successfully removed"}) 
