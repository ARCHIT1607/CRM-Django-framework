from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.


def home(request):
    order = Order.objects.all()
    customer = Customer.objects.all()

    total_customers = customer.count()
    total_orders = order.count()
    delivered = order.filter(status="Delivered").count()
    pending = order.filter(status="Pending").count()

    context = {'orders': order, 'customers': customer, 'total_customers': total_customers, 'total_orders': total_orders, 'delivered': delivered,
               'pending': pending}
    return render(request, 'accounts/dashboard.html', context)


def products(request):
    product = Product.objects.all()
    return render(request, 'accounts/products.html', {'products': product})


def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    order = customer.order_set.all()
    order_count = order.count()
    context = {'customer': customer,
               'orders': order, 'order_count': order_count}
    return render(request, 'accounts/customer.html', context)
