from django.shortcuts import render

def order(request):
    return render(request, 'order/orderPage.html')


def cart(request):
    return render(request, 'order/cartPage.html')