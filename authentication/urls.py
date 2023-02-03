from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
from .forms import LoginForm, PasswordResetForm

urlpatterns = [
    path('register', views.RegisterView.as_view(), name='register' ), 
    path('accounts/login', auth_view.LoginView.as_view(template_name= 'authenticate/login.html', authentication_form=LoginForm), name='login'),
    path('profile/', views.profileView.as_view(), name='profile'),
    path('password-reset/', auth_view.PasswordResetView.as_view(template_name= 'authenticate/PasswordReset.html', form_class=PasswordResetForm), name='password_reset')

]
