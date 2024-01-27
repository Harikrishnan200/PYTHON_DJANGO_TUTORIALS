from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login as userLogin,logout as userLogout  # in django login and logout are builtin functions
from django.contrib.auth import authenticate

# Create your views here.
def signUp(request):
    user = None
    error_message = None
    if request.POST:
        print('inside if')
        
        username = request.POST['username']
        password = request.POST['password']
        print(username,password)
        try:
            user = User.objects.create_user(username=username,password=password)
        except Exception as e:
            error_message = str(e)
    
    return render(request,'signup.html',{'user':user,'error_msg':error_message})

def login(request):
    error_message = None
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username,password = password) #authenticate() is an builtin function in django which is used to authenticate the user and its arguments are username and password of user        

        if user:
            #print(user)
            userLogin(request,user)  #argumemts of login fn are request object and user object
            return redirect('list') # arguments of redirect fn is name of the page that we want to redirect specified in urls.py


        else:
            print('invalid username')    





    return render(request,'login.html')



def logout(request):
    return render(request,'login.html')