from django.shortcuts import render
from django.http import HttpResponse
#from django.urls import reverse
import datetime


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def index(request):
    myvar = {'name': 'Abdulrhman', 'age': 33, 'sp': 'football'}
    # url = reverse('index')
    return render(request, 'gold.html', myvar)


def newPrice(request):
    #url = reverse('new')
    return render(request, 'new_price.html')
