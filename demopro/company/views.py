from django.shortcuts import render
from .models import register

# Create your views here.
# Create your views here.

def registerpage(request):
    if request.method =='POST':
        getName=request.POST.get('Name')
        getAddress = request.POST.get('Address')
        getUsername = request.POST.get('Username')
        getPassword = request.POST.get('Password')
        users = register()
        users.Name = getName
        users.Address = getAddress
        users.Username = getUsername
        users.Password = getPassword
        users.save()
    return render(request,'registerpage.html')