from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about/", views.about, name="Aboutus"),
    path("contact/", views.contact, name="Contact"),
    path("product/<int:pdid>", views.productview, name="productview"),
    path("tracker/", views.tracker, name="Trackingstatus"),
    path("search/", views.search, name="Search"),
    path("checkout/", views.checkout, name="Checkout"),

]