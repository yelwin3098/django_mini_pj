from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('register',views.register,name="user-register-page"),
    path('login',auth_views.LoginView.as_view(template_name="user/login.html"),
    name="user-login-page"),
    path('logout',auth_views.LogoutView.as_view(template_name="user/logout.html"),
    name="user-logout-page"),
    path('profile',views.profile,name="user-profile-page")
]