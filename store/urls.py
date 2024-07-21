from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("register/", views.register_user, name="register"),
    path("product/<int:pk>", views.product_detail, name="product"),
    path("category/<str:foo>", views.category, name="category"),  # Add URL for category page here.
]
