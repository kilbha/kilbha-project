from django.shortcuts import render,redirect
from django.contrib.auth.models import User
# Create your views here.
def LoginPage(request):
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