from django.shortcuts import render,redirect
from .forms import Register
from django.http import HttpResponse
from django.views import View
from .models import UserModel

def register(request):
    if request.session.get("email"):
        return redirect("/product/home/")
    form_ = Register()
    return render(request,"register.html",{"form":form_})

def afterregister(request):
    if request.method == "GET":
        return redirect("/users/register/")
    elif request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password') 
        try:
            obj = UserModel.objects.get(email=email)
        except:
            UserModel.objects.create(firstname=firstname, lastname=lastname, email=email, password=password)
            msg="Success fully login.. login to continue..."
            return render(request,"register.html", {"msg" : msg})                   
        else:
            msg = "User Already Exist..."
            return render(request,"register.html", {"msg" : msg}) 
        return redirect("/users/register/")
    

def login(request):
    if request.method == "GET":
        return redirect("/users/register/")
    elif request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            obj = UserModel.objects.get(email=email)
        except:
            msg = "User Does not exits"
            form = Register()
            return render(request, "register.html",{"msg" : msg, "form": form})
        else:
            if password == obj.password:
                request.session['email'] = email
                return redirect("/product/home/")
            else:
                msg = "Invalid password"
                form = Register()
                return render(request, "register.html", {"msg" : msg, "form" : form})
    else:
        return render (request,"register.html")


# Create your views here.  