from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, views
from maltlager.models import malt, hops, maltchange, hopschange, board_member, activity
from maltlager.forms import MaltForm, UpdateMaltForm, HopsForm, UpdateHopsForm, CreateUserForm, BoardMemberForm, ActivityForm
from django.utils import timezone
import django.db
import os

def bad_request(request):
    context = {'active_page': 'bad_request'}
    return render(request, 'maltlager/400.html', {})

def page_not_found(request):
    context = {'active_page': 'page_not_found'}
    return render(request, 'maltlager/404.html', {})

def server_error(request):
    context = {'active_page': 'server_error'}
    return render(request, 'maltlager/500.html', {})

def access_denied(request):
    context = {'active_page': 'access_denied'}
    return render(request, 'maltlager/access_denied.html', context)

def index(request):
    context = {'active_page': 'home'}
    return render(request, 'maltlager/index.html', context)

def about(request):
    context = {'active_page': 'about'}
    return render(request, 'maltlager/about.html', context)

def activities(request):
    activity_list = activity.objects.all().order_by('-date')
    context = {'active_page': 'activities', 'activity_list': activity_list}
    return render(request, 'maltlager/activities.html', context)

def edit_activity(request, activity_id):
    if request.user.is_staff:
        if request.method == 'POST':
            form = ActivityForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                form_title = data.get('title')
                form_date = data.get('date')
                form_content = data.get('content')
                try:
                    a = activity.objects.get(id=activity_id)
                    if a:
                        a.title = form_title
                        a.date = form_date
                        a.content = form_content
                        a.save()
                except:
                    a = activity(title=form_title,date=form_date,content=form_content)
                    a.save()
                return HttpResponseRedirect('/activities/')
            else:
                return HttpResponseRedirect('/invalid_form/')
        else:
            try:
                a = activity.objects.get(id=activity_id)
                if a:
                    data = {'title': a.title, 'date': a.date, 'content': a.content}
                    form = ActivityForm(initial=data)
                else:
                    form = ActivityForm()
            except:
                form = ActivityForm()
            context = {'form': form, 'active_page': 'activities', 'activity_id': activity_id}
            return render(request, 'maltlager/edit_activity.html', context)
    else:
        return HttpResponseRedirect('/access_denied/')

def delete_activity(request, activity_id):
    if request.user.is_staff:
        try:
            a = activity.objects.get(id=activity_id)
            a.delete()
            return HttpResponseRedirect('/activities/')
        except:
            return HttpResponseRedirect('/activities/')
    else:
        return HttpResponseRedirect('/access_denied/')

def members(request):
    bm = board_member.objects.all().order_by('name')
    context = {'active_page': 'members', 'board_member_list': bm}
    return render(request, 'maltlager/members.html', context)

def edit_board_member(request, board_member_id):
    if request.user.is_staff:
        if request.method == 'POST':
            form = BoardMemberForm(request.POST, request.FILES)
            if form.is_valid():
                data = form.cleaned_data
                form_image = request.FILES['image']
                form_name = data.get('name')
                form_role = data.get('role')
                form_description = data.get('description')
                try:
                    bm = board_member.objects.get(id=board_member_id)
                    if bm:
                        bm.name = form_name
                        bm.role = form_role
                        bm.description = form_description
                        bm.image = form_image
                        bm.save()
                except:
                    bm = board_member(name=form_name,role=form_role,description=form_description,image=form_image)
                    bm.save()
                return HttpResponseRedirect('/members/')
            else:
                return HttpResponseRedirect('/invalid_form/')
        else:
            try:
                bm = board_member.objects.get(id=board_member_id)
                if bm:
                    data = {'name': bm.name, 'role': bm.role, 'description': bm.description, 'image': bm.image}
                    form = BoardMemberForm(initial=data)
                else:
                    form = BoardMemberForm()
            except:
                form = BoardMemberForm()
            context = {'form': form, 'active_page': 'members', 'board_member_name': board_member_id}
            return render(request, 'maltlager/board_member.html', context)
    else:
        return HttpResponseRedirect('/access_denied/')

def delete_board_member(request, board_member_id):
    if request.user.is_staff:
        try:
            bm = board_member.objects.get(id=board_member_id)
            bm.delete()
            return HttpResponseRedirect('/members/')
        except:
            return HttpResponseRedirect('/members/')
    else:
        return HttpResponseRedirect('/access_denied/')

def contact(request):
    context = {'active_page': 'contact'}
    return render(request, 'maltlager/contact.html', context)

def calendar(request):
    context = {'active_page': 'calendar'}
    return render(request, 'maltlager/calendar.html', context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponseRedirect('/inactive_user/')
        else:
            return HttpResponseRedirect('/invalid_user/')
    else:
        form = AuthenticationForm(request)
        context = {'form': form, 'active_page': 'login'}
        return render(request, 'maltlager/login.html', context)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

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
            context = {'form': form, 'active_page': 'create_user'}
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
        context = {'user_list': users, 'active_page': 'settings'}
        return render(request, 'maltlager/settings.html', context)
    else:
        return HttpResponseRedirect('/access_denied/')
            
def user_exists(request):
    context = {'active_page': 'settings'}
    return render(request, 'maltlager/user_exists.html', context)

def list_malts(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/access_denied/')
    else:
        malt_list = malt.objects.all().order_by('name')
        context = {'malt_list': malt_list, 'active_page': 'maltlager'}
        return render(request, 'maltlager/malts.html', context)

def list_hops(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/access_denied/')
    else:
        hops_list = hops.objects.all().order_by('name')
        context = {'hops_list': hops_list, 'active_page': 'maltlager'}
        return render(request, 'maltlager/hops.html', context)

def history_malt(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/access_denied/')
    else:
        malt_change_list = maltchange.objects.all().order_by('-time')
        context = {'malt_change_list': malt_change_list, 'active_page': 'maltlager'}
        return render(request, 'maltlager/history_malt.html', context)

def history_hops(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/access_denied/')
    else:
        hops_change_list = hopschange.objects.all().order_by('-time')
        context = {'hops_change_list': hops_change_list, 'active_page': 'maltlager'}
        return render(request, 'maltlager/history_hops.html', context)

def malt_history(request,current_malt):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/access_denied/')
    else:
        malt_change_list = maltchange.objects.all().filter(name=current_malt).order_by('-time')
        context = {'malt_change_list': malt_change_list, 'current_malt': current_malt, 'active_page': 'maltlager'}
        return render(request, 'maltlager/malt_history.html', context)

def hops_history(request,current_hops):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/access_denied/')
    else:
        hops_change_list = hopschange.objects.all().filter(name=current_hops).order_by('-time')
        context = {'hops_change_list': hops_change_list, 'current_hops': current_hops, 'active_page': 'maltlager'}
        return render(request, 'maltlager/hops_history.html', context)

def malt_form(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/access_denied/')
    else:
        if request.method == 'POST':
            form = MaltForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                form_name = data.get('name')
                form_amount = data.get('amount')
                form_time = timezone.now()
                t = maltchange(name=form_name,amount=form_amount,time=form_time,user=request.user.username)
                t.save()
                m = malt(name=form_name,amount=form_amount)
                m.save()
                malt_list = malt.objects.all()
                context = {'malt_list': malt_list, 'active_page': 'maltlager'}
                return render(request, 'maltlager/malts.html',context)
        else:
            form = MaltForm()
            context = {'form': form, 'active_page': 'maltlager'}
        return render(request, 'maltlager/malt_form.html', context)

def hops_form(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/access_denied/')
    else:
        if request.method == 'POST':
            form = HopsForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                form_name = data.get('name')
                form_amount = data.get('amount')
                form_time = timezone.now()
                t = hopschange(name=form_name,amount=form_amount,time=form_time,user=request.user.username)
                t.save()
                h = hops(name=form_name,amount=form_amount)
                h.save()
                hops_list = hops.objects.all()
                context = {'hops_list': hops_list, 'active_page': 'maltlager'}
                return render(request, 'maltlager/hops.html',context)
        else:
            form = HopsForm()
        context = {'form': form, 'active_page': 'maltlager'}
        return render(request, 'maltlager/hops_form.html', context)

def update_malt_form(request, current_malt):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/access_denied/')
    else:
        if request.method == 'POST':
            form = UpdateMaltForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                form_change = data.get('amount')
                form_time = timezone.now()
                t = maltchange(name=current_malt,amount=form_change,time=form_time,user=request.user.username)
                t.save()
                m = malt.objects.get(name=current_malt)
                m.amount = m.amount + form_change
                m.save()
                malt_list = malt.objects.all()
                context = {'malt_list': malt_list, 'active_page': 'maltlager'}
                return render(request, 'maltlager/malts.html',context)
        else:
            form = UpdateMaltForm()
        amount = malt.objects.get(name=current_malt).amount
        context = {'form': form, 'current_malt': current_malt, 'amount': amount, 'active_page': 'maltlager'}
        return render(request, 'maltlager/update_malt_form.html', context)

def update_hops_form(request, current_hops):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/access_denied/')
    else:
        if request.method == 'POST':
            form = UpdateHopsForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                form_change = data.get('amount')
                form_time = timezone.now()
                t = hopschange(name=current_hops,amount=form_change,time=form_time,user=request.user.username)
                t.save()
                h = hops.objects.get(name=current_hops)
                h.amount = h.amount + form_change
                h.save()
                hops_list = hops.objects.all()
                context = {'hops_list': hops_list, 'active_page': 'maltlager'}
                return render(request, 'maltlager/hops.html',context)
        else:
            form = UpdateHopsForm()
        amount = hops.objects.get(name=current_hops).amount
        context = {'form': form, 'current_hops': current_hops, 'amount': amount, 'active_page': 'maltlager'}
        return render(request, 'maltlager/update_hops_form.html', context)
