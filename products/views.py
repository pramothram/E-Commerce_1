from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from products.models import Product


def home(request):
    return render(request, "index.html")


def product_list(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})

def categories(request):
    return render(request, "categories.html")


def contact(request):
    return render(request, "contact.html")


def fashion(request):
    return render(request, "fashion.html")


def electronics(request):
    return render(request, "electronics.html")


def footwear(request):
    return render(request, "footwear.html")


def home_appliances(request):
    return render(request, "home_appliances.html")


def books(request):
    return render(request, "books.html")


def sports(request):
    return render(request, "sports.html")


# REGISTER PAGE
def register(request):

    if request.method == "POST":

        fullname = request.POST.get("fullname")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        # Check password
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect("register")

        # Check email
        if User.objects.filter(username=email).exists():
            messages.error(request, "Email already exists.")
            return redirect("register")

        # Create user
        user = User.objects.create_user(
            username=email,
            first_name=fullname,
            email=email,
            password=password
        )

        messages.success(
            request,
            "Account created successfully. Please login."
        )

        return redirect("login")

    return render(request, "register.html")


# LOGIN PAGE
# LOGIN PAGE
def login_view(request):

    if request.method == "POST":

        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "")

        # If an old user session exists, clear it first
        if request.user.is_authenticated:
            logout(request)

        # Check email + password
        user = authenticate(
            request=request,
            username=email,
            password=password
        )

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect("home")

        else:
            messages.error(request, "Invalid email or password.")
            return redirect("login")

    return render(request, "login.html")
    

# LOGOUT
def logout_view(request):

    logout(request)

    return redirect("home")


# PAYMENT PAGE
def payment(request):

    return render(request, "payment.html")
