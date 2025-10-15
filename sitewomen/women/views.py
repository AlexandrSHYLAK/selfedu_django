from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect
from django.urls import reverse


# from jinja2 import Template

def index(request):
    return HttpResponse("Страница приложения women")

def categories(request, cat_id):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>id: {cat_id}</p>")

def categories_by_slug(request, cat_slug):
    # if request.GET:
    #     print(request.GET)
    if request.POST:
        print(request.POST)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>slug: {cat_slug}</p>")

def archive(request, year):
    if year > 2026:
        # raise Http404()
        # return redirect('/')
        # return redirect('/', permanent=True)
        # return redirect('index')
        # return redirect('home')
        # uri = reverse('cats', args=('music',))
        # return redirect('cats', 'music')
        uri = reverse('cats', args=('sport', ))
        # return redirect(uri)
        # return HttpResponsePermanentRedirect('/')
        return HttpResponseRedirect(uri)



    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
