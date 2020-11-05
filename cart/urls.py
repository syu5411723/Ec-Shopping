from django.urls import path, include
from . import views

app_name = 'cart'

urlpatterns = [
    path('cart/<int:pk>/', views.CartDetail.as_view(), name='cart_detail'),
]