from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home-page"),
    path("shop", views.shop, name="shop-page"),
    path("about", views.about, name="about-page"),
    path("contact", views.contact_form, name="contact-page"),
    path("contact_success", views.contact_success, name="contact_success"),
    path("feedback", views.feedback, name="feedback-page"),
    path('product/<slug:slug>/', views.product_detail, name='product-detail'),
]
