from django.urls import path
from . import views

urlpatterns = [
    path("", views.cart_view, name="cart"),
    path("add/<int:product_id>", views.add_to_cart, name="add_to_cart"),
    path("remove/<int:product_id>", views.remove_from_cart, name="remove_from_cart"),
    path("update/<int:product_id>/<int:quantity>", views.update_cart, name="update_cart"),
    # path("checkout/", views.checkout, name="checkout"),
    # path("payment/", views.payment, name="payment"),
    # path("complete/", views.complete, name="complete"),
    # path("cancel/", views.cancel, name="cancel"),
    # path("tracking/", views.tracking, name="tracking"),
    # path("history/", views.history, name="history"),
    # path("orders/<int:order_id>", views.order_detail, name="order_detail"),
    # path("order/cancel
]