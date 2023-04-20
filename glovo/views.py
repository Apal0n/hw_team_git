from django.shortcuts import render
from .models import Order
from django.http import HttpResponse


def order():
    orders = Order.objects.all()
    return HttpResponse(orders)
