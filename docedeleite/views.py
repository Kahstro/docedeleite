from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Doce de leite")

def novoDoce(request):
    return HttpResponse("Novo doce")

def leiteGoiaba(request):
    return HttpResponse("Doce de leite com goiaba")

def aindaTem(request):
    return HttpResponse("Ainda tem doce")