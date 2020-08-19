from django.shortcuts import render
from django.http import HttpResponse
import operator
# Create your views here.
def nothing(requests):
    return HttpResponse('<h1>Nothing to display here <br> Use /myhome or /myhobbies or /aboutus</h1>')
def home(requests):
    return render(requests,'wcount/myhome.html',{'Name':'World!!'})
def aboutus(requests):
    return render(requests,'wcount/aboutus.html',{'Name':'vasavi college of engineering','year':'3rd'})
def myhobbies(requests):
    return render(requests,'wcount/myhobbies.html')


