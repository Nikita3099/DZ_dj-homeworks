import csv
from django.core.paginator import Paginator
from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse

def index(request):
    return redirect(reverse('bus_stations'))

def bus_stations(request):
    with open(settings.BUS_STATION_CSV, encoding='utf-8') as file:
        reader = csv.DictReader(file)
        stations = list(reader)

    page_number = request.GET.get('page', 1)
    paginator = Paginator(stations, 10)
    page = paginator.get_page(page_number)

    context = {
        'bus_stations': page.object_list,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
