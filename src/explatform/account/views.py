#coding:UTF-8
from explatform.account.forms import UserRegisterForm
from django.template import loader, RequestContext
from django.shortcuts import render_to_response as rtr
from django.http import HttpResponse
def UserRegister(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            return HttpResponse('success')
    else:
        form = UserRegisterForm()
    t = loader.get_template('account_UserRegister.html')
    c = RequestContext(request, {'form':form})
    
    return HttpResponse(t.render(c))

def UserRegisterSuccess(request):
    return HttpResponse('success')