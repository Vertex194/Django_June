from django.urls import path
from . import views
from .views import about, make_reservation
import blog

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('home/', blog.views.home, name='home'), 
]