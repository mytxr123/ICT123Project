from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def menu_view(request):
    return render(request, "menu.html")

def pro_view(request):
    return render(request, "pro.html")

def re_view(request):
    return render(request, "re.html")

def contact_view(request):
    return render(request, "contact.html")

def cart_view(request):
    return render(request, "cart.html")

def order_view(request):
    return render(request, 'order.html')

from django.shortcuts import render, redirect
from .forms import OrderForm
from .models import Order
import json

def order_view(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        order_items = request.POST.get('order_items')
        total_price = request.POST.get('total_price')

        if form.is_valid():
            order = form.save(commit=False)
            order.order_items = order_items
            order.total_price = total_price
            order.save()
            return render(request, 'order_success.html', {'order': order})
    else:
        form = OrderForm()

    return render(request, 'order.html', {'form': form})



