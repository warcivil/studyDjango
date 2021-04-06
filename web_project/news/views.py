from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    print(request)
    return HttpResponse("hey")
def test(request):
    return HttpResponse("test url")