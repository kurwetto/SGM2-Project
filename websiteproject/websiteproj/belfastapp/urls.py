from django.urls import path
from belfastapp.views import *

app_name = 'belfastapp'
urlpatterns = [
    path('home', index, name='index'),
    path('testlang', testlang, name='testlang'),

]