from django.urls import path
from apps.main.views import index 
from . import views

urlpatterns = [
    path('', index, name='index'),  
]
urlpatterns = [
    path('', views.index, name='home'),  
    path('about/', views.about, name='about'),
]
