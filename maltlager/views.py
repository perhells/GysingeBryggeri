from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, views
from maltlager.models import malt, hops, maltchange, hopschange
from maltlager.forms import MaltForm, UpdateMaltForm, HopsForm, UpdateHopsForm, CreateUserForm
from django.utils import timezone
import django.db
import os

<<<<<<< HEAD
def bad_request(request):
    return render(request, 'maltlager/400.html', {})

def page_not_found(request):
    return render(request, 'maltlager/404.html', {})

def server_error(request):
    return render(request, 'maltlager/500.html', {})

=======
>>>>>>> a2ad41dd011fa5ed7e2e46536eeb23f1330bc54c
def index(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    else:
<<<<<<< HEAD
        malt_list = malt.objects.all().order_by('name')
        context = {'malt_list': malt_list}
        return render(request, 'maltlager/index.html', context)

def access_denied(request):
    context = {}
    return render(request, 'maltlager/access_denied.html', context)

=======
        malt_list = Malt.objects.all().order_by('name')
        context = {'malt_list': malt_list, 'username': request.user.username}
        return render(request, 'maltlager/index.html', context)

>>>>>>> a2ad41dd011fa5ed7e2e46536eeb23f1330bc54c
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
<<<<<<< HEAD
                #return index(request)
                return HttpResponseRedirect('/')
=======
                return index(request)
                # return HttpResponseRedirect('/')
>>>>>>> a2ad41dd011fa5ed7e2e46536eeb23f1330bc54c
            else:
                return HttpResponseRedirect('/inactive_user/')
        else:
            return HttpResponseRedirect('/invalid_user/')
    else:
        form = AuthenticationForm(request)
<<<<<<< HEAD
        context = {'form': form}
=======
        context = {'form': form, 'username': request.user.username}
>>>>>>> a2ad41dd011fa5ed7e2e46536eeb23f1330bc54c
        return render(request, 'maltlager/login.html', context)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

<<<<<<< HEAD
def create_user(request):
    if request.user.is_staff:
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                username = data.get('username')
                password = data.get('password')
                try:
                    user = User.objects.get(username=username)
                    if user:
                        return HttpResponseRedirect('/user_exists/')
                except:
                    user = User.objects.create_user(username=username, password=password)
                    user.save()
                return HttpResponseRedirect('/settings/')
            else:
                return HttpResponseRedirect('/invalid_form/')
        else:
            form = CreateUserForm()
            context = {'form': form}
            return render(request, 'maltlager/create_user.html', context)
    else:
        return HttpResponseRedirect('/access_denied/')

def delete_user(request, username):
    if request.user.is_staff:
        try:
            user = User.objects.get(username=username)
            user.delete()
            return HttpResponseRedirect('/settings/')
        except:
            return HttpResponseRedirect('/settings/')
    else:
        return HttpResponseRedirect('/access_denied/')

def grant_staff(request, username):
    if request.user.is_staff:
        try:
            user = User.objects.get(username=username)
            user.is_staff = True
            user.save()
            return HttpResponseRedirect('/settings/')
        except:
            return HttpResponseRedirect('/settings/')
    else:
        return HttpResponseRedirect('/access_denied/')

def revoke_staff(request, username):
    if request.user.is_staff:
        try:
            user = User.objects.get(username=username)
            user.is_staff = False
            user.save()
            return HttpResponseRedirect('/settings/')
        except:
            return HttpResponseRedirect('/settings/')
    else:
        return HttpResponseRedirect('/access_denied/')

def settings(request):
    if request.user.is_staff:
        users = User.objects.all().order_by('username')
        context = {'user_list': users}
        return render(request, 'maltlager/settings.html', context)
    else:
        return HttpResponseRedirect('/access_denied/')
            
def user_exists(request):
    context = {}
    return render(request, 'maltlager/user_exists.html', context)

def list_hops(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    else:
        hops_list = hops.objects.all().order_by('name')
        context = {'hops_list': hops_list}
=======
def hops(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    else:
        hops_list = Hops.objects.all().order_by('name')
        context = {'hops_list': hops_list, 'username': request.user.username}
>>>>>>> a2ad41dd011fa5ed7e2e46536eeb23f1330bc54c
        return render(request, 'maltlager/hops.html', context)

def history_malt(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    else:
<<<<<<< HEAD
        malt_change_list = maltchange.objects.all().order_by('-time')
        context = {'malt_change_list': malt_change_list}
=======
        malt_change_list = MaltChange.objects.all().order_by('-time')
        context = {'malt_change_list': malt_change_list, 'username': request.user.username}
>>>>>>> a2ad41dd011fa5ed7e2e46536eeb23f1330bc54c
        return render(request, 'maltlager/history_malt.html', context)

def history_hops(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    else:
<<<<<<< HEAD
        hops_change_list = hopschange.objects.all().order_by('-time')
        context = {'hops_change_list': hops_change_list}
=======
        hops_change_list = HopsChange.objects.all().order_by('-time')
        context = {'hops_change_list': hops_change_list, 'username': request.user.username}
>>>>>>> a2ad41dd011fa5ed7e2e46536eeb23f1330bc54c
        return render(request, 'maltlager/history_hops.html', context)

def malt_history(request,current_malt):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    else:
<<<<<<< HEAD
        malt_change_list = maltchange.objects.all().filter(name=current_malt).order_by('-time')
        context = {'malt_change_list': malt_change_list, 'current_malt': current_malt}
=======
        malt_change_list = MaltChange.objects.all().filter(name=current_malt).order_by('-time')
        context = {'malt_change_list': malt_change_list, 'current_malt': current_malt, 'username': request.user.username}
>>>>>>> a2ad41dd011fa5ed7e2e46536eeb23f1330bc54c
        return render(request, 'maltlager/malt_history.html', context)

def hops_history(request,current_hops):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    else:
<<<<<<< HEAD
        hops_change_list = hopschange.objects.all().filter(name=current_hops).order_by('-time')
        context = {'hops_change_list': hops_change_list, 'current_hops': current_hops}
=======
        hops_change_list = HopsChange.objects.all().filter(name=current_hops).order_by('-time')
        context = {'hops_change_list': hops_change_list, 'current_hops': current_hops, 'username': request.user.username}
>>>>>>> a2ad41dd011fa5ed7e2e46536eeb23f1330bc54c
        return render(request, 'maltlager/hops_history.html', context)

def malt_form(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    else:
        if request.method == 'POST':
            form = MaltForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                form_name = data.get('name')
                form_amount = data.get('amount')
                form_time = timezone.now()
<<<<<<< HEAD
                t = maltchange(name=form_name,amount=form_amount,time=form_time,user=request.user.username)
                t.save()
                m = malt(name=form_name,amount=form_amount)
                m.save()
                malt_list = malt.objects.all()
                context = {'malt_list': malt_list}
                return render(request, 'maltlager/index.html',context)
        else:
            form = MaltForm()
            context = {'form': form}
=======
                t = MaltChange(name=form_name,amount=form_amount,time=form_time,user=request.user.username)
                t.save()
                m = Malt(name=form_name,amount=form_amount)
                m.save()
                malt_list = Malt.objects.all()
                context = {'malt_list': malt_list, 'username': request.user.username}
                return render(request, 'maltlager/index.html',context)
        else:
            form = MaltForm()
            context = {'form': form, 'username': request.user.username}
>>>>>>> a2ad41dd011fa5ed7e2e46536eeb23f1330bc54c
        return render(request, 'maltlager/malt_form.html', context)

def hops_form(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    else:
        if request.method == 'POST':
            form = HopsForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                form_name = data.get('name')
                form_amount = data.get('amount')
                form_time = timezone.now()
<<<<<<< HEAD
                t = hopschange(name=form_name,amount=form_amount,time=form_time,user=request.user.username)
                t.save()
                h = hops(name=form_name,amount=form_amount)
                h.save()
                hops_list = hops.objects.all()
                context = {'hops_list': hops_list}
=======
                t = HopsChange(name=form_name,amount=form_amount,time=form_time,user=request.user.username)
                t.save()
                h = Hops(name=form_name,amount=form_amount)
                h.save()
                hops_list = Hops.objects.all()
                context = {'hops_list': hops_list, 'username': request.user.username}
>>>>>>> a2ad41dd011fa5ed7e2e46536eeb23f1330bc54c
                return render(request, 'maltlager/hops.html',context)
        else:
            form = HopsForm()
        
        return render(request, 'maltlager/hops_form.html', {'form': form})

def update_malt_form(request, current_malt):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    else:
        if request.method == 'POST':
            form = UpdateMaltForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                form_change = data.get('amount')
                form_time = timezone.now()
<<<<<<< HEAD
                t = maltchange(name=current_malt,amount=form_change,time=form_time,user=request.user.username)
                t.save()
                m = malt.objects.get(name=current_malt)
                m.amount = m.amount + form_change
                m.save()
                malt_list = malt.objects.all()
                context = {'malt_list': malt_list}
                return render(request, 'maltlager/index.html',context)
        else:
            form = UpdateMaltForm()
        amount = malt.objects.get(name=current_malt).amount
        context = {'form': form, 'current_malt': current_malt, 'amount': amount}
=======
                t = MaltChange(name=current_malt,amount=form_change,time=form_time,user=request.user.username)
                t.save()
                m = Malt.objects.get(name=current_malt)
                m.amount = m.amount + form_change
                m.save()
                malt_list = Malt.objects.all()
                context = {'malt_list': malt_list, 'username': request.user.username}
                return render(request, 'maltlager/index.html',context)
        else:
            form = UpdateMaltForm()
        amount = Malt.objects.get(name=current_malt).amount
        context = {'form': form, 'current_malt': current_malt, 'amount': amount, 'username': request.user.username}
>>>>>>> a2ad41dd011fa5ed7e2e46536eeb23f1330bc54c
        return render(request, 'maltlager/update_malt_form.html', context)

def update_hops_form(request, current_hops):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    else:
        if request.method == 'POST':
            form = UpdateHopsForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                form_change = data.get('amount')
                form_time = timezone.now(utc)
<<<<<<< HEAD
                t = hopschange(name=current_hops,amount=form_change,time=form_time,user=request.user.username)
                t.save()
                h = hops.objects.get(name=current_hops)
                h.amount = h.amount + form_change
                h.save()
                hops_list = hops.objects.all()
                context = {'hops_list': hops_list}
                return render(request, 'maltlager/hops.html',context)
        else:
            form = UpdateHopsForm()
        amount = hops.objects.get(name=current_hops).amount
        context = {'form': form, 'current_hops': current_hops, 'amount': amount}
=======
                t = HopsChange(name=current_hops,amount=form_change,time=form_time,user=request.user.username)
                t.save()
                h = Hops.objects.get(name=current_hops)
                h.amount = h.amount + form_change
                h.save()
                hops_list = Hops.objects.all()
                context = {'hops_list': hops_list, 'username': request.user.username}
                return render(request, 'maltlager/hops.html',context)
        else:
            form = UpdateHopsForm()
        amount = Hops.objects.get(name=current_hops).amount
        context = {'form': form, 'current_hops': current_hops, 'amount': amount, 'username': request.user.username}
>>>>>>> a2ad41dd011fa5ed7e2e46536eeb23f1330bc54c
        return render(request, 'maltlager/update_hops_form.html', context)
