from django import views
from django.urls import path
from .views import *

urlpatterns = [
    path('',view=index),
    path('enquiry/',view=contactform)
   
]