from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer
from .forms import CustomerForm

def addnew(request):
    return render(request, 'addnew.html')

def homepage(request):
    """
    Function response to website root HTTP requests

    Returns index.html template - db data returned

    """

    x = Customer.objects.all()


    return render(request, 'index.html', {'data': x})
