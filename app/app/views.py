from django.http import HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render
from django.template import loader

def home(request):
    return render(request, 'home/index.html')

def guide(request):
    return render(request, 'home/guide.html')

def robots_txt(request):
    return render(request, 'robots.txt', content_type='text/plain')

def error_404(request, exception):
    content = loader.render_to_string('home/404.html', {}, request)
    return HttpResponseNotFound(content)

def error_500(request):
    content = loader.render_to_string('home/500.html', {}, request)
    return HttpResponseServerError(content)

def error_403(request, exception):
    content = loader.render_to_string('home/500.html', {}, request)
    return HttpResponseServerError(content)

def error_400(request, exception):
    content = loader.render_to_string('home/500.html', {}, request)
    return HttpResponseServerError(content)