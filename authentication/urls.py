from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('home', views.home, name="home"),
    path('signin', views.signin, name ="signin"),
    path('signup', views.signup, name ="signup"),
    path('signout', views.signout, name ="signout"),
    path('after', views.after, name="after" ),
]