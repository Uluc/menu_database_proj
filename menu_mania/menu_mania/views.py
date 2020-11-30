from django.shortcuts import render
from django.views.decorators.cache import never_cache
from django.http import HttpResponse
from restaurant.models import Restaurant
from django.forms.models import model_to_dict
from django.core.serializers.json import DjangoJSONEncoder
import json


def home(request):
    restaurants_objs = Restaurant.objects.all()
    restaurant_list = []
    for a in restaurants_objs:
        street_address = a.address.streetAddress()
        a = model_to_dict(a)
        a['streetAddress'] = street_address
        restaurant_list.append(a)

    return render(request, 'menu_mania/homePage.html', {'restaurants': restaurant_list})
