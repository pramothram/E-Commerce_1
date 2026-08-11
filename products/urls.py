from django.urls import path
from . import views

urlpatterns = [

    path("", views.home, name="home"),

    path("products/", views.product_list, name="products"),

    path("categories/", views.categories, name="categories"),

    path("contact/", views.contact, name="contact"),

    path("fashion/", views.fashion, name="fashion"),

    path("electronics/", views.electronics, name="electronics"),

    path("footwear/", views.footwear, name="footwear"),

    path("home-appliances/", views.home_appliances, name="home_appliances"),

    path("books/", views.books, name="books"),

    path("sports/", views.sports, name="sports"),

    path("register/", views.register, name="register"),

    path("login/", views.login_view, name="login"),

    path("logout/", views.logout_view, name="logout"),

    path("payment/", views.payment, name="payment"),
]