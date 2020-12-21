from django.shortcuts import render
from django.forms.models import model_to_dict
from .models import Menu, Section, Dish
from restaurant.models import Restaurant


def menu(request, slug):
    restaurant = Restaurant.objects.get(id=slug)
    menu = Menu.objects.get(restaurant=restaurant)
    sections_list = []
    sections = Section.objects.filter(menu=menu)
    for section in sections:
        section_dict = model_to_dict(section)
        dishes_list = []
        dishes = section.dish_set.all()
        for dish in dishes:
            dish = model_to_dict(dish)
            dishes_list.append(dish)
        section_dict['dishes'] = dishes_list
        sections_list.append(section_dict)
    return render(request, 'menu/menuPage.html', {'restaurant': model_to_dict(restaurant), 'menu': model_to_dict(menu), 'sections': sections_list})