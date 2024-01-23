from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse


def index(req):
    return JsonResponse('Hello World', safe=False)

def about(req):
    return JsonResponse('Hello Worldddddd', safe=False)


