from django.urls import include, path
from .views import homepage,showpost

urlpatterns = [
    path('', homepage, name='blog'),
    path('/post/<slug:slug>/', showpost, name='showpost'),
]