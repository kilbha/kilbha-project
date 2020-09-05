from django.shortcuts import render

# Create your views here.
def HomePage(request):
    return render(request,'feed/Feed Page.html')