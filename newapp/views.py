from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    """
    Function response to website root HTTP requests

    Returns index.html template - db data returned
    """
    return render(request, 'index.html')
