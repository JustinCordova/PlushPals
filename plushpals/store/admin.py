from django.contrib import admin
from .models import Product, Feedback

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