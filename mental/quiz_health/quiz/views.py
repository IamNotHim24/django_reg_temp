from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.http import HttpResponse
from .forms import UserRegistrationForm

# Create your views here.

@login_required
def index(request):
    if not request.user.is_authenticated:
        return HttpResponse("Not authenticated")
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect('quiz')
    else:
        form = UserRegistrationForm()
    return render(request,'registration/register.html',{'form':form})
