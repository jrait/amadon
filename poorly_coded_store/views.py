from django.shortcuts import render, redirect
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def process(request):
    quantity_from_form = int(request.POST["quantity"])
    product = Product.objects.get(id = int(request.POST['product_id']))
    total_charge = quantity_from_form * product.price
    print("Charging credit card...")
    Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
    return redirect("/checkout")

def checkout(request):
    total_orders = Order.objects.all()
    total_spent = 0
    total_count = 0
    for order in total_orders:
        total_spent += order.total_price
        total_count+=1
    
    context = {
        'last_order':Order.objects.last(),
        'total_spent':total_spent,
        'total_count':total_count
    }
    return render(request,"store/checkout.html",context)