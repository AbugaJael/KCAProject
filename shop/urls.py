from django.urls import path
from . import views



urlpatterns = [
    path("", views.index, name="index"),
    path("cart/", views.cart, name="cart"),
    path("checkout/", views.checkout, name="checkout"),
    path("update_item/", views.updateItem, name="update_item"),
    path("product_view/<int:myid>/", views.product_view, name="product_view"),
    path("search/", views.search, name="search"),
    path("tracker/", views.tracker, name="tracker"),
    path("contact/", views.contact, name="contact"),
    path("loggedin_contact/", views.loggedin_contact, name="loggedin_contact"),

    path("register/", views.register, name="register"),
    path("registerbsn/", views.registerbsn, name="registerbsn"),
    path("change_password/", views.change_password, name="change_password"),
    path("login/", views.Login, name="login"),
    path("logout/", views.Logout, name="logout"),
    # path("analytics/", views.analytics, name="analytics"),
    # path('data', views.pivot_data, name='pivot_data'),
    
]