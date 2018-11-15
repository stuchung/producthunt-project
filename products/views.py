from django.shortcuts import render
import datetime

# Create your views here.

def home(request):
    time = datetime.datetime.today()
    return render(request, 'products/home.html',{'time':time})
