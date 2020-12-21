
from address.models import Address
from customer.models import Customer
from menu.models import Menu, Section, Dish
from order.models import Cart, Purchase
from ..models import Restaurant
# from ...restaurant.models import Restaurant
def run():

    Address.objects.all().delete()
    Customer.objects.all().delete()
    Menu.objects.all().delete()
    Section.objects.all().delete()
    Dish.objects.all().delete()
    Cart.objects.all().delete()
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
    }, {
        'street_address': '6767 Durdam Street',
        'zipcode': 70812
    }, {
        'street_address': '12 Privet Drive',
        'zipcode': 70889
    }, {
        'street_address': '12 Patriot Place',
        'zipcode': 99999
    }, {
        'street_address': '1 Arrowhead Drive',
        'zipcode': 56231
    }, {
        'street_address': '6934 Willard Street',
        'zipcode': 54587
    },{
        'street_address': '60 Pine Street',
        'zipcode': 54082
    }]

    for address in address_list:
        address = Address(state='LA',
                        street_address=address['street_address'],
                        zipcode=address['zipcode']
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
        {
            'name': 'McDonald\'s',
            'genre': 'American',
            'price_range': '$',
            'rating': 1.2,
            'open_time': '0:00',
            'close_time': '0:00'
        },
        {
            'name': 'James',
            'genre': 'Italian',
            'price_range': '$$',
            'rating': 4.2,
            'open_time': '10:00',
            'close_time': '18:00'
        },
        {
            'name': 'Denny\'s',
            'genre': 'American',
            'price_range': '$',
            'rating': 3.5,
            'open_time': '7:00',
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
        {
            'first_name': 'Matt',
            'last_name': 'Wilcox',
        },
        {
            'first_name': 'Andrew',
            'last_name': 'Hannie',
        },
        {
            'first_name': 'Bryce',
            'last_name': 'Lee',
        },
    ]

    addresses = Address.objects.all()
    x = 1
    y = 0
    for address in addresses:
        if x%2 == 0:
            customer = Customer(first_name=customer_list[y]['first_name'],
                                last_name=customer_list[y]['last_name'],
                                address=address
                                )
            customer.save()
            y+=1
        else:
            restaurant = Restaurant(name=restaurant_list[y]['name'],
                                    food_genre=restaurant_list[y]['genre'],
                                    price_range=restaurant_list[y]['price_range'],
                                    rating=restaurant_list[y]['rating'],
                                    open_time=restaurant_list[y]['open_time'],
                                    close_time=restaurant_list[y]['close_time'],
                                    address=address
                                    )
            restaurant.save()
            menu = Menu(restaurant=restaurant, bio="Basic menu bio")
            menu.save()
        x+=1

    section_list = ['lunch', 'dinner', 'drinks', 'appetizers', 'desserts']

    menus = Menu.objects.all()



    # make a list of dinner objects
    dinner_dishes = [
        {
            'name': 'hot dog',
            'description': 'A hot dog with ketchup and mustard',
            'price': 5.95,
            'ingredients': ['hot dog', 'mustard', 'ketchup', 'bun'],
        },
        {
            'name': 'hamburger',
            'description': 'A piece of ground beef between two buns',
            'price': 5.95,
            'ingredients': ['ground beef', 'lettuce', 'tomato', 'pickles', 'mustard', 'ketchup', 'bun'],
        },
        {
            'name': 'BLT',
            'description': 'A sandwich made out of bacon lettuce and tomato',
            'price': 6.95,
            'ingredients': ['bread', 'bacon', 'lettuce', 'tomato'],
        },
        {
            'name': 'grilled chicken',
            'description': 'chicken that is grilled',
            'price': 9.99,
            'ingredients': ['chicken'],
        },
        {
            'name': 'red beans and rice',
            'description': 'a southern classic',
            'price': 10.99,
            'ingredients': ['red beans', 'rice'],  
        },
        {
            'name': 'beef wellington',
            'description': 'filet mignon wrapped in a puff pastry',
            'price': 13.95,
            'ingredients': ['filet mignon', 'pastry'],
        },
        {
            'name': 'krabby patty',
            'description': 'spongebobs favorite',
            'price': 8.95,
            'ingredients': ['ground beef', 'mustard', 'ketchup', 'bun'],
        },
        {
            'name': 'steak',
            'description': 'a nice piece of beef that is cooked to your liking',
            'price': 16.50,
            'ingredients': ['steak'],
        },
        {
            'name': 'crawfish',
            'description': 'boiled crawfish',
            'price': 11.95,
            'ingredients': ['water', 'crawfish', 'spices'],
        }
    ]
    # make a list of lunch objects
    lunch_dishes = [
        {
            'name': 'hot dog',
            'description': 'A hot dog with ketchup and mustard',
            'price': 5.95,
            'ingredients': ['hot dog', 'mustard', 'ketchup', 'bun'],

        },
        {
            'name': 'hamburger',
            'description': 'A piece of ground beef between two buns',
            'price': 5.95,
            'ingredients': ['ground beef', 'lettuce', 'tomato', 'pickles', 'mustard', 'ketchup', 'bun'],
        },
        {
            'name': 'red beans and rice',
            'description': 'a southern classic',
            'price': 10.99,
            'ingredients': ['red beans', 'rice'],  
        },
        {
            'name': 'steak',
            'description': 'a nice piece of beef that is cooked to your liking',
            'price': 16.50,
            'ingredients': ['steak'],
        },
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
        {
            'name': 'Abita Amber',
            'description': 'louisiana wheat lager',
            'price': 5.85,
            'ingredients': ['Wheat']
        },
        {
            'name': 'Diet Coke',
            'description': 'Diet Cola',
            'price': 2.95,
            'ingredients': ['Diet Coke']
        },
        {
            'name': 'Sprite Cranberry',
            'description': 'Spirte with Cranberry',
            'price': 2.95,
            'ingredients': ['Sprite', 'Cranberry']
        },
        {
            'name': 'Bud Light',
            'description': 'light beer',
            'price': 4.00,
            'ingredients': ['Beer']
        },
        {
            'name': 'Dr. Pepper',
            'description': 'Cola',
            'price': 2.95,
            'ingredients': ['Dr. Pepper']
        },
        {
            'name': 'Diet Dr. Pepper',
            'description': 'Diet Cola',
            'price': 2.95,
            'ingredients': ['Diet Dr. Pepper']
        },
        {
            'name': 'Kool-Aid',
            'description': 'Water with lots of sugar',
            'price': 1.50,
            'ingredients': ['sugar', 'water', 'kool-aid']
        },
    ]

    # make an appetizer list
    app_list = [
        {
            'name':'Spring Rolls',
            'description': 'Classic style veggie Spring Roll',
            'price': 8.95,
            'ingredients': ['carrots', 'rice wrap', 'cabbage', 'onion', 'soy sauce']
        },
        {
            'name':'Quesadilla',
            'description': 'Classic cheese quesadilla',
            'price': 4.95,
            'ingredients': ['tortilla', 'cheese']
        }
    ]

    # make a dessert list
    dessert_list = [
        {
            'name':'ice cream',
            'description': 'vanilla ice cream with chocolate sauce and a cherry',
            'price': 4.95,
            'ingredients': ['ice cream', 'chocolate sauce', 'cherry']
        },
        {
            'name':'cheesecake',
            'description': 'Classic New York cheesecake',
            'price': 6.95,
            'ingredients': ['cheesecake', 'gramcracker']
        }
    ]

    for menu in menus:
        for section in section_list:
            section = Section(title=section, menu=menu)
            section.save()
            if section.title in 'drinks':
                for dish in drink_list:
                    if not Dish.objects.filter(name=dish['name'],description=dish['description'],price=dish['price'],ingredients=dish['ingredients']).exists():
                        dish = Dish(name=dish['name'],
                                    description=dish['description'],
                                    price=dish['price'],
                                    ingredients=dish['ingredients']
                                    )
                        dish.save()
                        dish.section.add(section)
                        dish.save()
                    else:
                        dish = Dish.objects.get(name=dish['name'],description=dish['description'],price=dish['price'],ingredients=dish['ingredients'])
                        dish.section.add(section)
                        dish.save()
            elif section.title in 'dinner':
                for dish in dinner_dishes:
                    if not Dish.objects.filter(name=dish['name'],description=dish['description'],price=dish['price'],ingredients=dish['ingredients']).exists():
                        dish = Dish(name=dish['name'],
                                    description=dish['description'],
                                    price=dish['price'],
                                    ingredients=dish['ingredients']
                                    )
                        dish.save()
                        dish.section.add(section)
                        dish.save()
                    else:
                        dish = Dish.objects.get(name=dish['name'],description=dish['description'],price=dish['price'],ingredients=dish['ingredients'])
                        dish.section.add(section)
                        dish.save()
            elif section.title in 'lunch':
                for dish in lunch_dishes:
                    if not Dish.objects.filter(name=dish['name'],description=dish['description'],price=dish['price'],ingredients=dish['ingredients']).exists():
                        dish = Dish(name=dish['name'],
                                    description=dish['description'],
                                    price=dish['price'],
                                    ingredients=dish['ingredients']
                                    )
                        dish.save()
                        dish.section.add(section)
                        dish.save()
                    else:
                        dish = Dish.objects.get(name=dish['name'],description=dish['description'],price=dish['price'],ingredients=dish['ingredients'])
                        dish.section.add(section)
                        dish.save()
            elif section.title in 'appetizers':
                for dish in app_list:
                    if not Dish.objects.filter(name=dish['name'],description=dish['description'],price=dish['price'],ingredients=dish['ingredients']).exists():
                        dish = Dish(name=dish['name'],
                                    description=dish['description'],
                                    price=dish['price'],
                                    ingredients=dish['ingredients']
                                    )
                        dish.save()
                        dish.section.add(section)
                        dish.save()
                    else:
                        dish = Dish.objects.get(name=dish['name'],description=dish['description'],price=dish['price'],ingredients=dish['ingredients'])
                        dish.section.add(section)
                        dish.save()
            else:
                for dish in dessert_list:
                    if not Dish.objects.filter(name=dish['name'],description=dish['description'],price=dish['price'],ingredients=dish['ingredients']).exists():
                        dish = Dish(name=dish['name'],
                                    description=dish['description'],
                                    price=dish['price'],
                                    ingredients=dish['ingredients']
                                    )
                        dish.save()
                        dish.section.add(section)
                        dish.save()
                    else:
                        dish = Dish.objects.get(name=dish['name'],description=dish['description'],price=dish['price'],ingredients=dish['ingredients'])
                        dish.section.add(section)
                        dish.save()
