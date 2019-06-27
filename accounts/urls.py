from django.urls import path
from .views import register, user_login,user_logout,profile


urlpatterns = [
    path('register/', register,name='register'),
    # path('', check),
    path('logout/', user_logout,name='logout'),
    path('login/', user_login, name='login'),
    path('profile/',profile)

]
