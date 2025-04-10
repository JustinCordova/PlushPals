from django import forms
from .models import Feedback 

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ["user_name", "user_email", "rating", "message"]
        labels = {
            "user_name": "Your Name",
            "user_email": "Your Email",
            "rating": "How would you rate your experience?",
            "message": "Your Feedback"
        }
