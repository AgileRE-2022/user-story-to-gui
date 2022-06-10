from django.urls import path
from . import views
#from django.urls import admin #

from . import views

urlpatterns = [
   path('', views.index, name="index"),
   #path('newstory', views.newstory, name="newstory"),
]