"""todoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers
from todos.views import TodoViewSet

#create a router, this will return an array of routes
router = routers.DefaultRouter()
#register viewset make it a RAW STRING.
router.register(r'todos', TodoViewSet)

urlpatterns = [
    #include here puts all the urls into an array, and checks if the route hit matches the url in the router array. It knows it matches, because it's in the router.register statement
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
