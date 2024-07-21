from django.shortcuts import render, redirect
from .models import Product, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from access.forms import RegisterUserForm, ProfileForm


# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, "store/home.html", {"products": products})


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Logged In")
            return redirect("home")
        else:
            messages.success(request, "Error logging in")
            return redirect("login")
    return render(request, "store/login.html")


def register_user(request):
    if request.method == "POST":
        user_form = RegisterUserForm(request.POST)
        profile_form = ProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            # user.set_password(user_form.cleaned_data['password'])
            user.save()
            # user = authenticate(username=username, password=password)

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request, "New Account Created")

            username = user_form.cleaned_data.get("username")
            password = user_form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Error registering user, please try again")
            return redirect("register")
    else:
        user_form = RegisterUserForm()
        profile_form = ProfileForm()
    return render(
        request,
        "store/registration.html",
        {"user_form": user_form, "profile_form": profile_form},
    )


def product_detail(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, "store/product.html", {"product": product})


def logout_user(request):
    logout(request)
    messages.success(request, "Logged Out")
    return redirect("home")

def category(request, foo):
    foo = foo.replace("-", " ") #replacing hyphens with spaces

    try:
        category = Category.objects.get(name=foo)
        product = Product.objects.get(category=category)
        return render(request, "store/category.html", {"product": product, "category": category})
    except:
        messages.success(request, "The category selected is not available") 
        return redirect("home")
