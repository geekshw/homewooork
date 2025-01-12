from django.shortcuts import render
from apps.main.models import Main, Contact, Awarts, About, Form

# Create your views here.
def index(requset):
    main = Main.objects.all()
    return render(requset, 'index.html', locals())
    
def about(requset):
    awarts = Awarts.objects.all()
    about = About.objects.latest("id")
    return render(requset, 'about.html', locals())

def contact(request):
    contact = Contact.objects.all()
    
    return render(request, 'contact.html', locals())