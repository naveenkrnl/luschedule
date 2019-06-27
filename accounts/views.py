from django.contrib.auth import login, get_user_model, logout
from django.shortcuts import render
from .forms import UserCreationForm, UserLoginForm
from django.http import HttpResponseRedirect, Http404

User=get_user_model()

# def check(request):
#     if request.user.is_authenticated:
#         return HttpResponseRedirect('/notes')
#     else:
#         return HttpResponseRedirect('/register')    

def profile(request):
    context={}
    return render(request,'profiles/profile_page.html',context)










def register(request, *args, **kwargs):
    form=UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/login')
    return render(request, 'accounts/register.html', {'form':form})

def user_login(request, *args, **kwargs):
    form=UserLoginForm(request.POST or None)
    if form.is_valid():
        user_obj=form.cleaned_data.get('user_obj')  
        print(user_obj)           
        login(request, user_obj)
        return HttpResponseRedirect('/')
    return render(request, 'accounts/login.html', {'form':form})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login')