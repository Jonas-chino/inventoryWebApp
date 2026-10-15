
# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Order
from .forms import OrderForm

def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.product = product
            order.save()
            return redirect('order_success', order_pk=order.pk)
    else:
        form = OrderForm()
        
    return render(request, 'shop/product_detail.html', {'product': product, 'form': form})

def order_success(request, order_pk):
    order = get_object_or_404(Order, pk=order_pk)
    return render(request, 'shop/order_success.html', {'order': order})