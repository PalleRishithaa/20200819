from django.shortcuts import render
from django.http import HttpResponse
#from django.urls import path
import operator
# Create your views here.
def food(requests):
    return HttpResponse('<h1> Do not eat junk food</h1>')
def drinks(requests):
    return HttpResponse('<h1> Drink 3 L water everyday</h1>')
def nothing(requests):
    return HttpResponse('<h1> Use /foods or /drinks</h1>')
