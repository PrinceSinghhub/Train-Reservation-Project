from django.shortcuts import render
from requests import request

# Create your views here.

def Index(request):
    
    return render(request,'index.html')