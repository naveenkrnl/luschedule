from django.forms import formset_factory, modelformset_factory
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Goal
from .forms import GoalForm,AddNewForm,DeleteForm



@login_required(login_url='/login/')
def home(request):
        context={}
        goals=Goal.objects.filter(user=request.user)
        context['goals']=goals
        # Main table form handler
        GoalModelFormset = formset_factory(GoalForm,extra=goals.count())
        formset = GoalModelFormset(request.POST or None)
        for form in formset:
                if form.is_valid():
                        goal_t=form.cleaned_data.get('goal_t')
                        goal=Goal.objects.get(goal_text=goal_t)
                        print(goal_t)
                        if form.cleaned_data.get('monday'):
                                goal.monday=form.cleaned_data.get('monday')
                        if form.cleaned_data.get('tuesday'):
                                goal.tuesday=form.cleaned_data.get('tuesday')
                        if form.cleaned_data.get('wednesday'):
                                goal.wednesday=form.cleaned_data.get('wednesday')
                        if form.cleaned_data.get('thursday'):
                                goal.thursday=form.cleaned_data.get('thursday')
                        if form.cleaned_data.get('friday'):
                                goal.friday=form.cleaned_data.get('friday')
                        if form.cleaned_data.get('saturday'):
                                goal.saturday=form.cleaned_data.get('saturday')
                        if form.cleaned_data.get('sunday'):
                                goal.sunday=form.cleaned_data.get('sunday')
                        goal.efficiency=int((int(goal.monday)+int(goal.tuesday)+int(goal.wednesday)+int(goal.thursday)+int(goal.friday)+int(goal.saturday)+int(goal.sunday))/7*100)
                        goal.save()
        context['formset']=formset
        return render(request,'sch/home.html',context)

@login_required(login_url='/login/')
def addgoal(request):
        context={}


        goals=Goal.objects.filter(user=request.user)
        context['goals']=goals
        form1=DeleteForm(request.POST or None)
        if form1.is_valid():
                goal_t1=form1.cleaned_data.get('goal_t1')
                goal=Goal.objects.get(goal_text=goal_t1)
                goal.delete()                
        # formset of adding goals
        form=AddNewForm(request.POST or None)
        if form.is_valid(): 
                goal_text1=form.cleaned_data.get('goal_text1')
                goal_text2=form.cleaned_data.get('goal_text2')
                goal_text3=form.cleaned_data.get('goal_text3')
                goal_text4=form.cleaned_data.get('goal_text4')
                goal_text5=form.cleaned_data.get('goal_text5')
                if(goal_text1):
                        new_goal=Goal.objects.get_or_create(goal_text=goal_text1,user=request.user)
                if(goal_text2):
                        new_goal=Goal.objects.get_or_create(goal_text=goal_text2,user=request.user)
                if(goal_text3):
                        new_goal=Goal.objects.get_or_create(goal_text=goal_text3,user=request.user)
                if(goal_text4):
                        new_goal=Goal.objects.get_or_create(goal_text=goal_text4,user=request.user)
                if(goal_text5):
                        new_goal=Goal.objects.get_or_create(goal_text=goal_text5,user=request.user)
        context['form']=form
        return render(request,"sch/add.html",context)