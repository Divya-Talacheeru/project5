from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def divya1_app1(request):
    return HttpResponse('<h1>view1 of app1</h1>')


def divya2_app2(request):
    return HttpResponse('<h1>view2 of app1</h1>')
