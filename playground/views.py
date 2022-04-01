from django.shortcuts import render


# from django.http import HttpResponse
# Create your views here.

def calculate():
    y = 1
    x = 2
    return x+y

def say_hello(request):
    x = calculate()
    return render(request, 'hello.html', {'name': 'MySZR'})
