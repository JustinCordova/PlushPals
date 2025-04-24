from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to="product_images/", blank=True)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Feedback(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_name} ({self.rating}/5)"
