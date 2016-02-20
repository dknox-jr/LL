from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.


def index(request):
    template = loader.get_template('main/index.html')
    context = {}
    return HttpResponse(template.render(context, request))
    
def user(request):
    template = loader.get_template('main/user.html')
    context = {}
    return HttpResponse(template.render(context, request))
    
def vendor(request):
    template = loader.get_template('main/vendor.html')
    context = {}
    return HttpResponse(template.render(context, request))
    
def articles(request):
    template = loader.get_template('main/articles.html')
    context = {}
    return HttpResponse(template.render(context, request))
    
def testimonials(request):
    template = loader.get_template('main/testimonials.html')
    context = {}
    return HttpResponse(template.render(context, request))