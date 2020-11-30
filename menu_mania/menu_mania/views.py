from django.shortcuts import render
from django.views.decorators.cache import never_cache
from django.http import HttpResponse


def home(request):
    """ Show active and pending projects to users allowed to work/view them and send down all completed projects """
    return render(request, 'menu_mania/homePage.html')
