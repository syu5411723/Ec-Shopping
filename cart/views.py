from django.shortcuts import render
from .models import Cart
from django.views.generic import DetailView


class CartDetail(DetailView):
    model = Cart
    template_name = 'cart/shopping_cart.html'
