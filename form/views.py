from django.shortcuts import render,HttpResponse
from django.contrib import messages
from .models import Form

def form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        Phone_number = request.POST.get('Phone_number')
        age = request.POST.get('age')
        queries = request.POST.get('query')
        forms=Form(name=name,email=email,phone_number=Phone_number,age=age,queries=queries)
        forms.save()
        return render(request,'form/form2.html')
    return render(request,'form/form.html')
    
def form_view(request):
        data=Form.objects.all()
        context={
             'data':data
         }
        return render(request,'form/form1.html',context)