from django.urls import path, include
from user import views



urlpatterns = [
    path('SignUp/', views.SignUp, name='SignUp'),
    path('SignIn/', views.SignIn, name='SignIn'),

]
