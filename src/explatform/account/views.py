#coding:UTF-8
from django.shortcuts import render_to_response as rtr
def Register(request):
    return rtr('account/Register.html',{'greeting':'hello world'})

