from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):
    #home 
    
    home = Home.objects.latest('updated')
    
    #About
    about = About.objects.latest('updated')
    profiles = Profile.objects.filter(about=about)
    
    #Skilss
    categories = Category.objects.all()
    
    #portofolio
    portfolios = Portfolio.objects.all()
    
    context = {
        'home':home,
        'about':about,
        'profiles': profiles,
        'categories':categories,
        'portfolios':portfolios,
    }
    return render(request, "index.html",context)