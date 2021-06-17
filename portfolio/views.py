from django.shortcuts import render
from .models import Portfolio

# Create your views here.
def home(request):
    context = {
        'posts' : Portfolio.objects.all()
        }
    return render(request, 'portfolio/portfolio.html', context)

def blog(request):
    return render(request, 'blog/home.html')
