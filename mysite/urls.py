"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include


## explaination of paths

# path('', include('main.urls')) here we look for whatever inside the string or '', example it is a blank path or string.
# then uss blank path par kaha jaana hai use dekhenge, so blank path par kaha jaana hai woh main.urls main hai, there we again look iss blank path ka kya karna hai, because blank path ke aage kuchh nahi hai
# if path is start/home/, then
# path('start/', include('main.urls')) -> here ham half - half paths ko dekhenge, so now after start, we will look for home/, and home ko kaha dekhna hai woh start ke path main likha hai,i.e.  inside main.urls
# then in main.urls file we have another path for
# path('home/', views.home, name = "our_home/home")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls'))
]
