from django.shortcuts import render
from django.contrib.auth.models import User

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
