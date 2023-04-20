from django.shortcuts import render
from .models import Order
from django.http import HttpResponse

def main_page(request):
    return render(request, 'base.html')

def show_couriers(request):
    couriers = models.Courier.objects.all()
    return render(request, 'couriers.html', context={'couriers': couriers})

def order():
    orders = Order.objects.all()
    return HttpResponse(orders)
