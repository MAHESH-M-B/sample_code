from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login
# Create your views here.
from django.contrib.auth.models import User
from .models import user

def SignUp(request):
    if request.method == 'POST':
        fname = request.POST.get('first_name')
        lname = request.POST.get('last_name')
        uname = request.POST.get('username')
        email = request.POST.get('email')
        number = request.POST.get('phone_number')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            return HttpResponse('password and confirm password are not same')
        else:
            user = User.objects.create_user(uname, email, password1)
            user.save()
            return redirect('SignIn')
    return render(request, 'user/SignUp.html')


def SignIn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=password1)
        if user != None:
            login(request, user)
            return redirect('form')
        else:
            return HttpResponse('username or password is not correct')
    return render(request, 'user/SignIn.html')