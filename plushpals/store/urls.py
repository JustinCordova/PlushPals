from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home-page"),
    path("shop", views.shop, name="shop-page"),
    path("about", views.about, name="about-page"),
    path("contact", views.contact, name="contact-page"),
    path("feedback", views.feedback, name="feedback-page"),
    path('product/<slug:slug>/', views.product_detail, name='product-detail'),
]
