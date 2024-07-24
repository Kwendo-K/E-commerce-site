from django.shortcuts import render

# Create your views here.
def cart_view(request):
    return render(request, "cart/cart.html", {})

def add_to_cart(request):
    return render(request, "cart/cart.html", {})

def remove_from_cart(request):
    return render(request, "cart/cart.html", {})

def update_cart(request):
    return render(request, "cart/cart.html", {})