from django.contrib import admin 
from django.urls import path 
from . import views 


urlpatterns = [ 
	path('', views.process_text_view, name='query'), 

] 
