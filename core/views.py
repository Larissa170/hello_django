from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request,numero1,numero2):
    soma = numero1 + numero2
    return HttpResponse('<h1>Hello, a Soma é  {}.</h1>'.format(soma))
