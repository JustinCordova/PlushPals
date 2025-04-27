from django.contrib import admin
from .models import Product, Feedback, BusinessFeedback

# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_featured')  # Show in list view
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}  # Auto-fill slug from name
    list_filter = ('is_featured',)

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'rating', 'submitted_at')
    list_filter = ('rating', 'submitted_at')
    search_fields = ('user_name', 'user_email', 'message')

@admin.register(BusinessFeedback)
class BusinessFeedbackAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'user_email', 'submitted_at')  # Show in list view
    search_fields = ('user_name', 'user_email', 'message')  # Allow search by these fields
    list_filter = ('submitted_at',)  # Filter feedback by submission date