from django import forms
from .models import Feedback, BusinessFeedback

class BusinessFeedbackForm(forms.ModelForm):
    class Meta:
            model = BusinessFeedback
            fields = ['user_name', 'user_email', 'message']
            
    # Adding field labels and limitations (max_length, min_length)
    user_name = forms.CharField(
        max_length=100,  # Maximum length for name
        min_length=5,    # Minimum length for name
        label="Your Name",  # Custom label for user name
        help_text="Please enter your full name.",
    )
    user_email = forms.EmailField(
        label="Email Address",  # Custom label for email
        help_text="We will not share your email.",
    )
    message = forms.CharField(
        max_length=1000,  # Maximum length for the message
        label="Your Message",  # Custom label for the message
        help_text="Please provide detailed feedback (maximum 1000 characters).",
    )

    # Custom email validation
    def clean_email(self):
        email = self.cleaned_data.get('user_email')
        if '@example.com' in email:  # Restrict email domain as an example
            raise forms.ValidationError("We do not accept feedback from example.com addresses.")
        return email
            
