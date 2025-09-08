
from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import SignupForm
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
from .forms  import CustomLoginForm


# Create your views here.

def home(request):
    return render(request, "home.html")

def signup_view(request):
    if request.method =='POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request,"Account created!. You can login now")
            return redirect('login')
        else:
            return render(request,'auth/signup.html',{'form':form})
    else:
        form = SignupForm()
        return render(request,'auth/signup.html',{'form':form})
    
def user_login(request):
    if request.method=="POST":
        form = CustomLoginForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                request.session['username'] = user.username
                request.session['last_login'] = str(user.last_login)
                response = HttpResponseRedirect(reverse('home'))
                response.set_cookie(
                    'last_login_time',   # cookie name
                    str(user.last_login), # cookie value
                    max_age=3600         # expires in 1 hour
                )
                return response
            return render(request, 'auth/login.html', {'form': form})
    else:
        form = CustomLoginForm()
        return render(request,'auth/login.html',{'form':form})
                
def user_logout(request):
    logout(request)
    return redirect('login')
    
    
    
        