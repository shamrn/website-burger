from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.forms.utils import ErrorList


class UserRegistrationForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'input-login','placeholder':'Логин'})
        self.fields['email'].widget.attrs.update({'class': 'input-login', 'placeholder': 'E-mail'})

    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input-login','placeholder':'Пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input-login','placeholder':'Пароль еще раз'}))
    phone = forms.CharField(min_length=5,max_length=35)

    phone.widget.attrs.update({'class':'input-login','placeholder':'Номер'})

    class Meta:
        model = User
        fields = ('username','email')


    def clean_email(self):
        cd = self.cleaned_data
        object_list_email = Profile.objects.values_list('email',flat=True)
        if cd['email'] in object_list_email:
            raise forms.ValidationError('Пользователь с таким email уже существует, вы можете восстановить пароль')
        return cd['email']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароль не совпадает')
        return cd['password2']



class DivErrorList(ErrorList):
    def __str__(self):
        return self.as_divs()

    def as_divs(self):
        if not self: return ''
        return ''.join(['%s' % e for e in self])
