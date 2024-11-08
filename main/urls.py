from django.contrib import admin
from django.urls import path
from main import views

# Alternative way, '.' implies current directory(or the directory in which you are working.)
# from . import views 

urlpatterns = [
	path('',views.index, name = "index")

]
