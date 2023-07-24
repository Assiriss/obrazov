from django.shortcuts import render
from django.http import HttpResponse


def first(request):
    return HttpResponse('Страница прилодения Investment')

def lot(request, page_id):
    if page_id == 1:
        return HttpResponse(f'<big>ХАХАХАХАХ ЛОХ</big>')
    elif page_id == 2:
        return HttpResponse('<h2>не такой уж и лох</h2>')

def second(request):
    return HttpResponse('хахахахахахаха')
