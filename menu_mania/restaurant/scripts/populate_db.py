import os, sys, time
dir_path = str(os.path.dirname(os.path.realpath(__file__)))
dir_path = dir_path[:-16]
sys.path.insert(0, dir_path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'menu_mania.settings'
from django.conf import settings
import django
django.setup()

from address.models import Address
from customer.models import Customer
from menu.models import Menu, Section, Dish
from ...order.models import Order, Purchase
from ..models import Restaurant

Address.objects.all().delete()
Customer.objects.all().delete()
Menu.objects.all().delete()
Section.objects.all().delete()
Dish.objects.all().delete()
Order.objects.all().delete()
Purchase.objects.all().delete()
Restaurant.objects.all().delete()

address_list = [{
    'street_address': '123 First Street',
    'zipcode': 70820
}, {
    'street_address': '456 Second Street',
    'zipcode': 70820
}, {
    'street_address': '789 Third Street',
    'zipcode': 70820
}, {
    'street_address': '111 Fourth Street',
    'zipcode': 70803
}, {
    'street_address': '222 Fifth Street',
    'zipcode': 70803
}, {
    'street_address': '333 Sixth Street',
    'zipcode': 70803
}]

for address in address_list:
    address = Address(state='LA',
                    street_address=address.street_address,
                    zipcode=address.zipcode
                    )
    address.save()


restaurant_list = [
    {
        'name': 'Dominos',
        'genre': 'Pizza',
        'price_range': '$',
        'rating': 4,
        'open_time': '10:00',
        'close_time': '23:00'
    },
    {
        'name': 'John\'s',
        'genre': 'American',
        'price_range': '$$',
        'rating': 3,
        'open_time': '11:00',
        'close_time': '22:00'
    },
    {
        'name': 'Sushi Masa',
        'genre': 'Japanese',
        'price_range': '$$$',
        'rating': 5,
        'open_time': '10:30',
        'close_time': '21:00'
    },
]
customer_list = [
    {
        'first_name': 'Ryan',
        'last_name': 'Stephens',
    },
    {
        'first_name': 'Uluc',
        'last_name': 'Ozdenvar',
    },
    {
        'first_name': 'Jorie',
        'last_name': 'Noll',
    },
]

addresses = Address.objects.all()
x = 1
y = 0
for address in addresses:
    if x%2 == 0:
        customer = Customer(first_name=customer_list[y].first_name,
                            last_name=customer_list[y].last_name,
                            address=address
                            )
        customer.save()
        y+=1
    else:
        restaurant = Restaurant(name=restaurant_list[y].name,
                                genre=restaurant_list[y].genre,
                                price_range=restaurant_list[y].price_range,
                                rating=restaurant_list[y].rating,
                                open_time=restaurant_list[y].open_time,
                                close_time=restaurant_list[y].close_time,
                                address=address
                                )
        restaurant.save()
        menu = Menu(restaurant=restaurant, bio="Basic menu bio")
        menu.save()
    x+=1

section_list = ['lunch', 'dinner', 'drinks', 'appetizers', 'desserts']

menus = Menu.objects.all()

for menu in menus:
    for section in section_list:
        section = Section(title=section)
        section.save()

# make a list of dinner objects
dinner_dishes = [
    {
        'name': 'hot dog',
        'description': 'A hot dog with ketchup and mustard',
        'price': 5,
        'ingredients': ['hot dog', 'mustard', 'ketchup', 'bun'],

    }
]

# make a list of lunch objects
lunch_dishes = [
    {
        'name': 'hot dog',
        'description': 'A hot dog with ketchup and mustard',
        'price': 5,
        'ingredients': ['hot dog', 'mustard', 'ketchup', 'bun'],

    }
]


# make a drink list

drink_list = [
    {
        'name': 'Coke',
        'description': 'Cola',
        'price': 2.95,
        'ingredients': ['Coke']
    },
    {
        'name': 'Sprite',
        'description': 'lemon-lime soda',
        'price': 2.95,
        'ingredients': ['Sprite']
    },
    {
        'name': 'Sweet Tea',
        'description': 'sweetend house brewed Tea',
        'price': 2.95,
        'ingredients': ['Tea']
    },
]

# make an appetizer list
app_list = [
    {
        'name':'Spring Rolls',
        'description': 'Classic style veggie Spring Roll',
        'price': 8.95,
        'ingredients': ['carrots', 'rice wrap', 'cabbage', 'onion', 'soy sauce']
    }
]

# make a dessert list
dessert_list = [
    {
        'name':'ice cream',
        'description': 'vanilla ice cream with chocolate sauce and a cherry',
        'price': 4.95,
        'ingredients': ['ice cream', 'chocolate sauce', 'cherry']
    }
]


        # for x in range(len(dishes_list)):
