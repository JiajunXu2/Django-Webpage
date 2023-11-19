# essentually a requests handler
from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    context = {}
    return render(request, "E:/Projects-Python/Django-Webpage/django_webpage/home/templates/test.html", context)

def cart(request):
    context = {}
    return render(request, "E:/Projects-Python/Django-Webpage/django_webpage/home/templates/cart.html", context)

def checkout(request):
    context = {}
    return render(request, "E:/Projects-Python/Django-Webpage/django_webpage/home/templates/checkout.html", context)

#E:/Projects-Python/Django-Webpage/django_webpage/home/templates/test.html