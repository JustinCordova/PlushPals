from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True, db_index=True)  # Slug field
    price = models.DecimalField(max_digits=6, decimal_places=2)
    summary = models.CharField(max_length=255, blank=True, default='') 
    description = models.TextField()
    image = models.ImageField(upload_to="product_images/", blank=True)
    is_featured = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('product-detail', args=[self.slug])  # Use slug in URL
        # Slug just adds dashes (-) so the URL is cleaner

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Auto-format name and slug
        self.name = self.name.title()
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

# feedback for products
class Feedback(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='feedback_set')  # link to Product!
    user_name = models.CharField(max_length=100)
    # Email validator is automatically used, only add manually if you want to restrict a domain
    rating = models.IntegerField(
        choices=[(i, i) for i in range(1, 6)],
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_name} ({self.rating}/5)"
    
    def save(self, *args, **kwargs):
        # Trim overly long messages and add ellipsis
        if len(self.message) > 500:
            self.message = self.message[:497] + "..."
        super().save(*args, **kwargs)
        
# feedback for overall business
class BusinessFeedback(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.user_name}"

    def save(self, *args, **kwargs):
        # Optional: limit message length
        if len(self.message) > 1000:
            self.message = self.message[:997] + "..."
        super().save(*args, **kwargs)

