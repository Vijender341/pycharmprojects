from django.http import HttpResponse
from django.shortcuts import render

from myapp.models import *


def show_about_page(request):
    print("about page request")
    name = 'Youtube'
    link = "https://www.youtube.com"

    data={
        'name': name,
        'link' : link
    }
    return render(request, 'about.html',data)
def show_home_page(request):

    images = Image.objects.all()
    cats = Category.objects.all()

    data = {'images': images, 'category': cats}

    return  render(request, 'home.html', data)