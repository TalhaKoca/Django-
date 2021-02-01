from django.shortcuts import render, redirect
from .forms import RegisterForm,LoginForm

from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate, logout
# authenticate fonksiyonu kullanıcı varsa objesini dönecek, yoksa NoNe değerini dönecek..
# Create your views here.

def register(request):
    
    form = RegisterForm(request.POST or None)

    if form.is_valid(): # clean fonksiyonu çağrıldı...
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        newUser = User(username=username)
        newUser.set_password(password)
        newUser.save()

        login(request,newUser)
        messages.info(request,"Kayıt Başarıyla Gerçekleştirildi...")
        return redirect("index") # urls blog path name....

    context = {

            "form":form
        }
    return render(request,"register.html",context)

"""    if request.method == "POST":
        form = RegisterForm(request.POST) # posttan gelen bilgilerle doldurduk.
        if form.is_valid(): # clean fonksiyonu çağrıldı...

            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            
            newUser = User(username=username)
            newUser.set_password(password)
            newUser.save()

            login(request,newUser)
            return redirect("index") # urls blog path name....

        context = {

            "form":form
        }
        return render(request,"register.html",context)
    else:
        form = RegisterForm()
        context = {

            "form":form
        }
        return render(request,"register.html",context)"""

def loginUser(request):
    form = LoginForm(request.POST or None)

    context = {

        "form" : form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        # clean özel olarak yazmazsak kendisi gibi çalışacak.override yapmadık...
        
        user = authenticate(username=username,password =password)

        if user is None:
            messages.info(request,"Kullanıcı Adı veya Parola Hatalı")
            return render(request,"login.html",context)
        messages.success(request,"Başarıyla Giriş Yaptınız...")
        
        login(request,user) # kullanıcı sisteme giriş yaptı..
        return redirect("index")

    return render(request,"login.html",context)

def logoutUser(request):
    logout(request)
    messages.success(request,"Başarıyla Çıkış Yapıldı..")
    return redirect("index")