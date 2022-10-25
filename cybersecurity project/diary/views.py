from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.db import connection
from .models import DiaryEntry

import datetime
import cowsay

@login_required
def index(request):
    entry_list = DiaryEntry.objects.filter(owner=request.user).order_by('-entry_date')
    context = {'latest_entry_list': entry_list}
    return render(request, 'diary/index.html', context)

@login_required
#@csrf_protect
@csrf_exempt
def addEntryView(request):
    title = request.POST.get('entry_title')
    text = request.POST.get('entry_text')
    date = datetime.datetime.now()
    username = request.user
    if title:
        DiaryEntry.objects.create(entry_title=title,entry_text=text,entry_date=date,owner=username)
    return redirect('/diary')

@login_required
def detail(request, entry_id):
    entry = get_object_or_404(DiaryEntry, pk=entry_id)
    return render(request, 'diary/detail.html', {'entry': entry})
    #if entry.owner_id == request.user.id:
    #    return render(request, 'diary/detail.html', {'entry': entry})
    #else:
    #    return redirect('/diary')

@login_required
@csrf_protect
def searchEntryView(request):
    search_text = request.POST.get('search_text')
    cowsay.cow(search_text)
    with connection.cursor() as cursor:
        response = cursor.execute("SELECT id FROM diary_diaryentry WHERE entry_text LIKE '%%%s%%'" % (search_text)).fetchall()
    entry_str = str(response[0])[1:-2]
    entry_id = int(entry_str)
    #entry = DiaryEntry.objects.get(entry_text__contains=search_text)
    #entry_id = entry.id
    entry = get_object_or_404(DiaryEntry, pk=entry_id)
    return render(request, 'diary/detail.html', {'entry': entry})