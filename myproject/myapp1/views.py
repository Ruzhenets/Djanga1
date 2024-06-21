# Create your views here.
from django.http import HttpResponse
# from django.shortcuts import render


def index(request):
    a = '''
    <h1>My first Django site</h1>
    <p1>This site made with Django framework</p1>
    '''
    return HttpResponse("Hello, world!"+a)


def about(request):
    b = '''
    <h1>I am studying to use python to build sites easy way</h1>
    <p1>May be python helps me to keep ledger easier too</p1>
    '''
    return HttpResponse("About us"+b)
