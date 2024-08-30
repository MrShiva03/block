from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import  login, logout, authenticate



# Create your views here.
def index(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
    return render(request,'login.html')


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        # print(f'{username=}, {password=}, {email=}, {cpassword=}')
        if password == cpassword:
            try:
                user = User(username=username, email=email)
                user.set_password(password)
                user.save()
                return redirect('login')
            except:
                pass
    return render(request, 'register.html')

def logout_view(request):
    logout(request)
    return redirect('index')
