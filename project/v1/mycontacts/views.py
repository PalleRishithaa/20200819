from django.shortcuts import render
import operator
from django.http import HttpResponse

# Create your views here.
def nothing(requests):
    return HttpResponse('<h1>Use /phone or /email</h1>')
def phone(requests):
    return HttpResponse('<h1>My Phone number appears here</h1>')
def email(requests):
    return HttpResponse('<h1>My mail address appears here</h1>')


