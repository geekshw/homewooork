from django.shortcuts import render
from apps.main.models import Main 
# Create your views here.


def index(request):
    main = Main.objects.latest('id')
    return render(request, 'index.html' , locals())

def about(request):
    return render(request, 'about.html')


