from django import forms
from .models import Goal

class GoalForm(forms.Form):
    goal_t=forms.CharField(max_length=200,required=False)
    monday=forms.BooleanField(required=False)
    tuesday=forms.BooleanField(required=False)
    wednesday=forms.BooleanField(required=False)
    thursday=forms.BooleanField(required=False)
    friday=forms.BooleanField(required=False)
    saturday=forms.BooleanField(required=False)
    sunday=forms.BooleanField(required=False)    
    class Meta:
        fields = [
            'goal_t',
            # 'goal_text',
            'monday',
            'tuesday',
            'wednesday',
            'thursday',
            'friday',
            'saturday',
            'sunday'
        ]

class AddNewForm(forms.Form):
    goal_text1 = forms.CharField(label='Data', widget=forms.TextInput(attrs=
                                {
                                    'class':'form-control',
                                    'placeholder' : 'Your New Goal',
                                }),error_messages={
                                    "required": "Arree..!! Goal to bhardo"
                                }
                            )    
    goal_text2 = forms.CharField(label='Data', required=False,widget=forms.TextInput(attrs=
                                {
                                    'class':'form-control',
                                    'placeholder' : 'Your New Goal',
                                }))     
    goal_text3 = forms.CharField(label='Data',required=False, widget=forms.TextInput(attrs=
                                {
                                    'class':'form-control',
                                    'placeholder' : 'Your New Goal',
                                }))    
    goal_text4 = forms.CharField(label='Data',required=False, widget=forms.TextInput(attrs=
                                {
                                    'class':'form-control',
                                    'placeholder' : 'Your New Goal',
                                }))    
    goal_text5 = forms.CharField(label='Data',required=False, widget=forms.TextInput(attrs=
                                {
                                    'class':'form-control',
                                    'placeholder' : 'Your New Goal',
                                }))

class DeleteForm(forms.Form):
    goal_t1=forms.CharField(max_length=200)
    class Meta:
        fields=[
            'goal_t1'
        ]