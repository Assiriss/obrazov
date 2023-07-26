from django.shortcuts import render
from django.http import HttpResponse


def first(request):
    return HttpResponse('Страница прилодения Investment')

def lot(request, page_id):
    if page_id == 1:
        return HttpResponse(f'<big>ХАХАХАХАХ ЛОХ</big>')
    elif page_id == 2:
        return HttpResponse('<h2>не такой уж и лох</h2>')

def proba_comit(request, word):
    return HttpResponse(f'наше слово {word}')
def second(request):
    return HttpResponse(f"""
                    <a href="https://yandex.ru/search/?text=fatal%3A+failed+to+load+library+libcurl-4.dll+git&lr=213&clid=2270455&win=583&src=suggest_Tail">GHGHGHHGHG</a>
    """)
