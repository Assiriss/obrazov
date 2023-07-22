from django.shortcuts import render
from django.http import HttpResponse


def first(request):
    return HttpResponse('Страница прилодения Investment')

def lot(request):
    return HttpResponse("<h1>Привет бездари!</h1> "
                        "<p>gf gf gf gf </p> "
                        "<big>папапапапа</big>")
