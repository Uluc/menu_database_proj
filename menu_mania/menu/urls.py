from django.urls import path
from . import views

urlpatterns = [
    path('menu/<slug:slug>', views.menu, name='menu'),
]