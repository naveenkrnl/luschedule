from django.db.models import Q
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import get_user_model, authenticate
from .models import USERNAME_REGEX,BRANCH_CHOICES,SEMESTER_CHOICES
from django.core.validators import RegexValidator
 

User=get_user_model()

class UserLoginForm(forms.Form):
    query=forms.CharField(label='Username/Email',widget=forms.TextInput(attrs=
                                {
                                    'class':'form-control',
                                    'placeholder' : 'User Name',
                                }))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs=
                                {
                                    'class':'form-control',
                                    'placeholder' : 'Password',
                                }))
    def clean(self, *args,**kwargs):
        query =self.cleaned_data.get('query')
        password =self.cleaned_data.get('password')
        # the_user=authenticate(username=username, password=password)
        # if not the_user:
        #     raise forms.ValidationError("INvalid credentials")
        # user_qs1=User.objects.filter(username__iexact=query)
        # user_qs2=User.objects.filter(email__iexact=query)
        # user_qs_final=(user_qs1 | user_qs2).distinct()
        user_qs_final=User.objects.filter(
            Q(username__iexact=query)|
            Q(email__iexact=query)
        ).distinct()
        if not user_qs_final.exists() and user_qs_final.count() !=1:
            raise forms.ValidationError("Invalid username")
        else:
            user_obj =user_qs_final.first()
            if not user_obj.check_password(password):
                raise forms.ValidationError("Invalid Password for {}".format(query))
            # if not user_obj.is_active:
            #     raise forms.ValidationError("User not active")
        self.cleaned_data['user_obj']=user_obj
        return super(UserLoginForm, self).clean(*args,**kwargs)


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    name = forms.CharField(label='Password', widget=forms.TextInput(attrs=
                                {
                                    'class':'form-control',
                                    'placeholder' : 'A Unique Username to identify you !',
                                }))
    rollno = forms.CharField(label='Password', widget=forms.TextInput(attrs=
                                {
                                    'class':'form-control',
                                    'placeholder' : '1216243',
                                }))                                
    username = forms.CharField(label='Password', widget=forms.TextInput(attrs=
                                {
                                    'class':'form-control',
                                    'placeholder' : 'Username',
                                }))
    email = forms.CharField(label='Password', widget=forms.TextInput(attrs=
                                {
                                    'class':'form-control',
                                    'placeholder' : 'College email id ending with @jmit.ac.in',
                                }))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs=
                                {
                                    'class':'form-control',
                                    'placeholder' : 'Password',
                                }))
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(attrs=
                                {
                                    'class':'form-control',
                                    'placeholder' : 'Confirm Password',
                                }))
    branch = forms.ChoiceField(choices = BRANCH_CHOICES, widget=forms.Select(attrs=
                                {
                                    'class':'form-control',
                                }), required=True)
    semester = forms.ChoiceField(choices = SEMESTER_CHOICES, widget=forms.Select(attrs=
                                {
                                    'class':'form-control',
                                }), required=True)

    class Meta:
        model = User
        fields = ('username','name','rollno','email','branch','semester')

    def clean_email(self):
        email=self.cleaned_data.get("email")
        if 'jmit.ac.in' not in email:
            raise forms.ValidationError("Only JMIT Students with College Email ID can Register")
        return email
    def clean_rollno(self):
        rollno=self.cleaned_data.get("rollno")
        print(len(rollno))
        if len(rollno) != 7:
            raise forms.ValidationError("Sahi Roll Number Daalo Yaar")
        return rollno
    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        # user.is_active=False
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password','is_staff', 'is_active')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]