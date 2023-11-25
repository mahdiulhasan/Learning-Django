from django.shortcuts import render,redirect
from django.contrib.auth.models import auth
from django.contrib import messages

# Create your views here.
def login_page(request):
    print(request)
    if request.method == 'GET':   
        return render(request, 'login.html')
    elif request.method == 'POST':
        input_username = request.POST['username']   
        input_password = request.POST['password']
        print(input_username,input_password)
        
        # auth.authenticate(username=input_username,password=input_password)
        # print(auth.authenticate(username=input_username,password=input_password))
        user = auth.authenticate(username=input_username,password=input_password)
        print(user)
        
        if user is not None:
            auth.login(request,user)
            return redirect('deshboard')
        else:
            messages.error(request,'username or password didnot match')
            return render(request, 'login.html')
        
        