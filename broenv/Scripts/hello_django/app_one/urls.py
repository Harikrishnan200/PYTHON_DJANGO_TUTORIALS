
from django.urls import path,include
from . import views


urlpatterns = [
    
    path('',views.home,name='home'),
    path('create/',views.create,name='create'),
    path('list/',views.list,name='list'),
    path('edit/<pk>',views.edit,name='edit'),
    path('movie/',views.movies,name='movies'),
    path('delete/<pk>',views.delete,name='delete'),
    

]
