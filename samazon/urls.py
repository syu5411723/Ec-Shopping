from django.urls import path, include
from . import views

app_name = 'samazon'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('post_list', views.PostList.as_view(), name='post_list'),
    path('post_detail/<int:pk>/', views.PostDetail.as_view(), name='post_detail')
]