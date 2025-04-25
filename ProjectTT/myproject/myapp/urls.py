from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index),
    path('menu/', views.menu_view, name='menu'),
    path('pro/', views.pro_view, name='pro'),
    path('re/', views.re_view, name='re'),
    path('contact/', views.contact_view, name='contact'),
    path('cart/', views.cart_view, name='cart'),
    path('order/', views.order_view, name='order'),
    
]