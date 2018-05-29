from __future__ import unicode_literals
from django.shortcuts import render
from .models import *

def index(request):
    return render(request,"index.html",{})
def sign_up(request):
    if request.method!="POST":
        return render(request, "register.html", {'sign_up': "You Can SignUp Here"})
    user_obj = User.objects.create(username=request.POST['username'],email=request.POST['email'],
                                   first_name = request.POST['first_name'],
                                   last_name = request.POST['last_name'],)
    user_obj.set_password(request.POST['password'])
    user_obj.save()
    User_Info.objects.create(user=user_obj,middle_name=request.POST['middle_name'])
    return render(request, "registration_success.html", {'success':"Your Account was successfully registered. "
                                                        "Now You can Login to Your Account"})



def log_in(request):
    return render(request,"login.html",{'login':"You Can login Here"})
