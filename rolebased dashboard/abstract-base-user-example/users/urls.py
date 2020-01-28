from django.urls import path,include
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
				
				#alternative way to include authentication views
				path('', auth_views.LoginView.as_view(), name='login'),
   				path('',include('django.contrib.auth.urls')),
   				path('login_success', views.login_success, name='login_success'),
				#path('signup/', views.SignUp.as_view(), name='signup'),
				

		 ]
#