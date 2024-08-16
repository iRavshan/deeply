from django.http import HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render
from django.template import loader

def home(request):
    return render(request, 'home/index.html')

def guide(request):
    return render(request, 'home/guide.html')

def error_404(request, exception):
    content = loader.render_to_string('home/404.html', {}, request)
    return HttpResponseNotFound(content)

def error_500(request):
    content = loader.render_to_string('home/500.html', {}, request)
    return HttpResponseServerError(content)