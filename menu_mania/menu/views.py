from django.shortcuts import render
from .models import Menu
from restaurant.models import Restaurant


def menu(request, slug):
    restaurant = Restaurant.objects.get(id=slug)
    menu = Menu.objects.get(restaurant=restaurant)
    return render(request, 'menu/menuPage.html')