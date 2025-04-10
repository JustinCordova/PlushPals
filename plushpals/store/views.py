from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'store/index.html')

def shop(request):
    return render(request, 'store/shop.html')

def about(request):
    return render(request, 'store/about.html')

def contact(request):
    return render(request, 'store/contact.html')

def feedback(request):
    return render(request, 'store/feedback.html')

def custom_404(request, exception):
    return render(request, '404.html', status=404)