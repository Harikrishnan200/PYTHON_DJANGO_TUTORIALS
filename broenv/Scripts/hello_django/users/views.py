from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def signUp(request):
    user = None
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        print(username,password)
       # user = User.objects.create_user(username=username,password=password)

    return render(request,'signup.html',{'user_obj':user})
