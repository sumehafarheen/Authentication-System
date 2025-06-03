from django.urls import path, include
from .views import authView,home
from django.contrib.auth.views import LogoutView


app_name ="base"

urlpatterns =[
    path("", home, name="home"),
    path("signup/", authView, name="authView"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("logout/", LogoutView.as_view(), name="logout"),    
]