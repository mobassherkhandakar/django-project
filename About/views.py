from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def about_us(req):
    name = 'Mobassher Khandakar'
    age = 23
    offering = {'nm': name, 'year': age}
    return render(req, 'about/about.html', context=offering)
