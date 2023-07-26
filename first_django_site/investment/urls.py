from django.urls import path
from .views import *



urlpatterns = [
    path('', first),
    path('lot/<int:page_id>/', lot),
    path('proba_comit/<str:word>/', proba_comit),
    path('second/', second)





]