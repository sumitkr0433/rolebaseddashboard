from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm




# #######################33
# def login(request):
#   if request.method == 'POST':
#     username = request.POST['username']
#     password = request.POST['password']

#     user = auth.authenticate(username=username, password=password)

#     if user is not None:
#       auth.login(request, user)
#       messages.success(request, 'You are now logged in')
#       return redirect('dashboard')
#     else:
#       messages.error(request, 'Invalid credentials')
#       return redirect('login')
#   else:
#     return render(request, 'accounts/login.html')














#########################333333




# def login_success(request):
#     """
#     Redirects users based on whether they are in the admins group
#     """
   

def login_success(request):
    if request.user.is_authenticated and request.user.role=='employee':
            return render(request, 'user/dashboard.html')
    elif request.user.is_authenticated and request.user.role=='manager':
        	return render(request, 'user/dashboard1.html')
    elif  request.user.is_authenticated and request.user.role=='operation':
    	
        	return render(request, 'user/dashboard3.html')