from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Feedback
from .forms import BusinessFeedbackForm

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

    if request.method == "POST":
        user_name = request.POST.get('user_name')
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')

        if user_name and rating and comment:
            Feedback.objects.create(
                product=product,
                user_name=user_name,
                rating=rating,
                message=comment
            )
            return redirect('product-detail', slug=product.slug)

    # get all feedback for the product
    feedback_list = product.feedback_set.all()

    #calculate average
    if feedback_list:
        avg_rating = sum(feedback.rating for feedback in feedback_list) / len(feedback_list)
    else:
        avg_rating = 0 # no reviews, no ratings
    
    range_list = list(range(1, 6))
    
    return render(request, 'store/product_detail.html', {
        'product': product,
        'feedback_list': feedback_list,
        'avg_rating': avg_rating,
        'range_list': range_list,
    })


def contact_form(request):
    
    form = BusinessFeedbackForm()
    
    if request.method == "POST":
        form = BusinessFeedbackForm(request.POST)

        if form.is_valid():
            # Save to the BusinessFeedback model
            BusinessFeedback.objects.create(
                user_name=form.cleaned_data['user_name'],
                user_email=form.cleaned_data['user_email'],
                message=form.cleaned_data['message']
            )
            # Redirect to a success page after form submission
            return redirect('contact_success')
        else:
            form=BusinessFeedbackForm()

    return render(request, 'store/contact.html', {'form': form})

def contact_success(request):
    return render(request, 'store/contact_success.html')
