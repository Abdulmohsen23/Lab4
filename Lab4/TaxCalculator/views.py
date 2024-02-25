from django.shortcuts import render
from django.http import HttpResponse

tax_rate = 15
tax = 0.15
# Create your views here.
def index(request):
    return HttpResponse("This is a site to calculate tax.")


def anyNumber(request, number):
    return HttpResponse(f'The total is  {number * (tax+1)}')


def taxRate(request):
    return render(request, "TaxCalculator/taxRate.html",{
        "tax": tax_rate
    })