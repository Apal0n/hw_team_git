from django.shortcuts import render
from .models import Order
from django.http import HttpResponse


def order(request):
    orders = Order.objects.all()
    return orders(HttpResponse)
