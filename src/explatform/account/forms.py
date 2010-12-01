#coding:UTF-8
from django import forms
class UserRegisterForm(forms.Form):
    '''用户注册表单
    '''
    NickName = forms.CharField(max_length=20, min_length=4, widget=forms.TextInput)
    Email = forms.EmailField()#max_length=75)
    Password = forms.CharField(max_length=40, min_length=6 , widget=forms.PasswordInput)
    
    def clean(self):
        cd = self.cleaned_data
        _Email = cd.get('Email')
        print _Email