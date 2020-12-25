from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .models import *
from .forms import OrderForm
from .filters import OrderFilter
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

    myFilter = OrderFilter(request.GET, queryset=order)
    order = myFilter.qs
    context = {'customer': customer,
               'orders': order, 'order_count': order_count, 'myFilter': myFilter}
    return render(request, 'accounts/customer.html', context)


def createOrder(request, pk):
    OrderFormSet = inlineformset_factory(Customer, Order,
                                         fields=('product', 'status'))
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)
    # form = OrderForm(initial={'customer': customer})
    if request.method == 'POST':
        # print('Printing POST :', request.POST)
        # form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    context = {'formset': formset}
    return render(request, 'accounts/order_form.html', context)


def updateOrder(request, pk):

    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        # print('Printing POST :', request.POST)
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)


def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        # print('Printing POST :', request.POST)
        order.delete()
        return redirect('/')

    context = {'item': order}
    return render(request, 'accounts/delete.html', context)
