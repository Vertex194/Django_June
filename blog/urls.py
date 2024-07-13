from django.urls import path, include
from . import views
from .views import index, make_reservation,reservation_success,about
from mainsite.views import homepage,showpost

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('blog/', homepage, name='blog'),
    path('make_reservation/', views.make_reservation, name='make_reservation'),
    path('success/', views.reservation_success, name='reservation_success'),
    path('reservation_success/<int:email_sent>/', reservation_success, name='reservation_success'),
    path('post/<slug:slug>/', showpost, name='showpost'),
]