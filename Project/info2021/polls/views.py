from django.shortcuts import render
from django.http import HttpResponse

def noticias(request):
    return HttpResponse("Las noticias del dia")

# Create your views here.
