from django.shortcuts import render
from phones.models import Phone


def show_catalog(request):
    sort_param = request.GET.get('sort', '')

    if sort_param == 'name':
        phones = Phone.objects.order_by('name')
    elif sort_param == 'min_price':
        phones = Phone.objects.order_by('price')
    elif sort_param == 'max_price':
        phones = Phone.objects.order_by('-price')
    else:
        phones = Phone.objects.all()

    return render(request, 'catalog.html', {'phones': phones})


def show_phone(request, slug):
    phone = Phone.objects.get(slug=slug)
    return render(request, 'phone.html', {'phone': phone})
