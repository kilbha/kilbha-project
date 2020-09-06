from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from feedarea.forms import QuestionInputForm
from .models import QuestionInput
# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    form = QuestionInputForm()
    if request.method == 'POST':
        form = QuestionInputForm(request.POST)
        form_inst = form.save(commit=False)
        form_inst.rand_url = form_inst.Question.replace(' ','-')
        form_inst.Author = request.user
        form_inst.save()
        return redirect('home')
    else:
        Questions = QuestionInput.objects
        return render(request,'feed/Feed Page.html',{'form':form,'Questions':Questions})

def YesCounter(request,prk):
    return redirect('home')

def NoCounter(request,prk):
    return redirect('home')
