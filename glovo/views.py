from django.shortcuts import render, HttpResponse
from . import models


def main_page(request):
    return render(request, 'base.html')


def show_couriers(request):
    couriers = models.Courier.objects.all()
    return render(request, 'couriers.html', context={'couriers': couriers})
