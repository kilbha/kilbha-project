from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def LoginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            userobj = str(User.objects.get(email=request.POST['logemail']))
            user = authenticate(request,username=userobj,password=request.POST['logpassword'])
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return render(request,'accounts/login.html',{"error":"Email or password is incorrect."})
        else:
            return render(request,'accounts/login.html')
def SignUpPage(request):
    if request.method == 'POST':
        if User.objects.filter(username=request.POST["username"]).exists() or User.objects.filter(email=request.POST["regemail"]).exists():
            return render(request,'accounts/signup.html',{"error":"Email is already registered."})
        else:
            user = User.objects.create_user(request.POST['username'],email=request.POST['regemail'],password=request.POST['regpassword'])
            name = request.POST['name']
            user.first_name = name
            user.save()
            return redirect('login')
    else:
        return render(request,'accounts/signup.html')
def LogOutPage(request):
    logout(request)
    return redirect('login')