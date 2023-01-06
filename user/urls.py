from django.urls import path, include
from user import views



urlpatterns = [
    path('SignUp/', views.signup, name='SignUp'),
    path('SignIn/', views.signin, name='SignIn'),

]
