from django.shortcuts import render
from .models import Book

def books_view(request):

    books = Book.objects.all().order_by('pub_date')  # Сортируем по дате публикации
    return render(request, 'books/books_list.html', {'books': books})
def books_by_date_view(request, pub_date):
    books = Book.objects.filter(pub_date=pub_date).order_by('name')

    prev_date = Book.objects.filter(pub_date__lt=pub_date).order_by('-pub_date').values_list('pub_date', flat=True).first()
    next_date = Book.objects.filter(pub_date__gt=pub_date).order_by('pub_date').values_list('pub_date', flat=True).first()

    return render(request, 'books/books_by_date.html', {
        'books': books,
        'pub_date': pub_date,
        'prev_date': prev_date,
        'next_date': next_date,
    })
