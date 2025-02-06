from django.http import HttpResponse
from django.shortcuts import render
import os
import datetime

def home_view(request):
    """Главная страница со списком доступных маршрутов"""
    return render(request, 'home.html', {'routes': ['/', 'current_time/', 'workdir/']})

def current_time_view(request):
    """Вывод текущего времени"""
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return HttpResponse(f"Текущее время: {now}")

def workdir_view(request):
    """Вывод списка файлов в рабочей директории"""
    files = os.listdir('.')
    return HttpResponse('<br>'.join(files))
