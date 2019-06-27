from django.contrib import admin
from django.urls import path,include
from .views import home,addgoal
urlpatterns = [
    path("",home,name="home"),
    # path("test/",test,name="test"),
    path("goals/",addgoal,name="add")

]
