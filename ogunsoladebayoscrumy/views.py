from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def get_grading_parameters(request):
    return HttpResponse('Welcome to Django')
