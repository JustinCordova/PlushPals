from django.shortcuts import render, get_object_or_404
from .models import Product, Feedback

# Create your views here.

def home(request):
    featured_products = Product.objects.filter(is_featured=True)
    return render(request, 'store/index.html', {'featured_products': featured_products})

def shop(request):
    products = Product.objects.all()
    return render(request, 'store/shop.html', {'products': products})

def about(request):
    return render(request, 'store/about.html')

def contact(request):
    return render(request, 'store/contact.html')

def feedback(request):
    feedback_list = Feedback.objects.all().order_by('-submitted_at')  # latest first
    return render(request, 'store/feedback.html', {'feedback_list': feedback_list})

def custom_404(request, exception):
    return render(request, '404.html', status=404)

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug) 
    # Use slug instead of pk=pk because thats what we use in models
    # Using get_object_or_404 for automatic error handling, instead of .objects.get(...)
    return render(request, 'store/product_detail.html', {'product': product})