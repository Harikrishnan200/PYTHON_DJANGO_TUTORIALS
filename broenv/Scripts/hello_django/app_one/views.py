from django.shortcuts import render
from django.http import HttpResponse
from .models import MovieInfo
from .forms import MovieForm

# Create your views here.


def list(request):

   # print(request.COOKIES)
   # visits = int(request.COOKIES.get('visits',0)) #request.COOKIES.get('visits',0) this fn returns value in the form of string
   # visits = visits+1
    
   # count = request.session.get('count',0) # this fn returns value in the form of string
   # count = int(count)
   # count = count + 1
   # request.session['count'] = count
    
    
    movie_set = MovieInfo.objects.all()
    recent_visits = request.session.get('recent_visits',[])
    recent_movie_set = MovieInfo.objects.filter(pk__in = recent_visits)
    response = render(request,'list.html',{'mov':movie_set,'recent_movies':recent_movie_set}) #used in session
   # response = render(request,'list.html',{'mov':movie_set,'visits':visits}) # used in the case of cookies
   # response = render(request,'list.html',{'mov':movie_set,'visits':count})  # used in the case of session
   # response.set_cookie('visits',visits)
    return response

def edit(request,pk):
    instance_to_be_edited = MovieInfo.objects.get(pk=pk)
    if request.POST:
        """
        title = request.POST.get('title')
        year = request.POST.get('year')
        description = request.POST.get('description')
        instance_to_be_edited.title = title
        instance_to_be_edited.year = year
        instance_to_be_edited.description = description
        instance_to_be_edited.save()  """
        frm = MovieForm(request.POST,instance = instance_to_be_edited)
        if frm.is_valid():
            instance_to_be_edited.save()
        
    else: 
        
        frm = MovieForm(instance=instance_to_be_edited)

        recent_visits = request.session.get('recent_visits',[])
        recent_visits.insert(0,pk)
        request.session['recent_visits'] = recent_visits
        
        
        response = render(request,'create.html',{'frm':frm})


        

    return response

def home(request):
    sample ={
        'list': [

            'god_father.jpg',
            'aadu_1.webp',
            'god_father.jpg'



        ]
    }
    return render(request,'home.html',sample)

def movies(request):
    mov_dict = {
        'items':[
           {
        'title':'godfather',
        'summary':'story of an underworld king',
        'year':'2003',
        'sucess':False,
        'img':'god_father.jpg'
        },
        {
        'title':'titanic',
        'summary':'story of an underworld king',
        'year':'2003',
        'sucess':True,
        'img':'titanic.jpg'
        },
        {
        'title':'aadu',
        'summary':'',
        'year':'2003',
        'sucess':True,
        'img':'aadu_1.webp'
        } 
        ]
    }
    return render(request,'edit.html',mov_dict)
    

def create(request):
    
    frm = MovieForm()
    if request.POST:
        """
        title = request.POST.get('title')
        year = request.POST.get('year')
        description = request.POST.get('description')  
        MovieInfo_obj = MovieInfo(title=title,year=year,description=description)
        MovieInfo_obj.save()   """
        frm = MovieForm(request.POST,request.FILES)

        
        if frm.is_valid():
            frm.save()
            movie_set = MovieInfo.objects.all()
            

            return render(request,'list.html',{'mov':movie_set})

         
        else:
            print(frm.errors)
            frm = MovieForm()

    
    return render(request,'create.html',{'frm':frm})  

def delete(request,pk):
    instance = MovieInfo.objects.get(pk=pk)
    instance.delete()
    movie_set = MovieInfo.objects.all()
    return render(request,'list.html',{'mov':movie_set})  



