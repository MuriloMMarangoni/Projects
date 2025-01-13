from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def rasc(request):
    return render(request,'html.html')