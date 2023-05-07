from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Customer
from .forms import CustomerForm

def addnew(request):

    if request.method == 'POST':

        formset = CustomerForm(request.POST)

        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect("/")

    else:
        formset = CustomerForm()
        return render(request, 'addnew.html', {'formset': formset})

def homepage(request):
    """
    Function response to website root HTTP requests

    Returns index.html template - db data returned

    """

    x = Customer.objects.all()


    return render(request, 'index.html', {'data': x})
