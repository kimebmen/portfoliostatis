from django.shortcuts import render, get_object_or_404

from .models import Job

# Create your views here.
def home(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs': jobs})

def detail1(request):    
    return render(request, 'jobs/detail1.html')

def detail2(request):    
    return render(request, 'jobs/detail2.html')

def detail3(request):    
    return render(request, 'jobs/detail3.html')

def detail4(request):    
    return render(request, 'jobs/detail4.html')

def detail5(request):    
    return render(request, 'jobs/detail5.html')

def detail6(request):    
    return render(request, 'jobs/detail6.html')

def detail7(request):    
    return render(request, 'jobs/detail7.html')

def detail8(request):    
    return render(request, 'jobs/detail8.html')

def detail9(request):    
    return render(request, 'jobs/detail9.html')

def detail10(request):    
    return render(request, 'jobs/detail10.html')

def detail11(request):    
    return render(request, 'jobs/detail11.html')

