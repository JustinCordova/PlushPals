from django import forms
from .models import Feedback, BusinessFeedback

class BusinessFeedbackForm(forms.ModelForm):
    class Meta:
        model = BusinessFeedback
        fields = ['user_name', 'user_email', 'message']
        
        labels = {
            'user_name': 'Your Name',
            'user_email': 'Email Address',
            'message': 'Your message',
        }
        help_texts = {
            'user_name': 'Please enter your full name.',
            'user_email': 'We will not share your email.',
            'message': 'Please provide detailed feedback (maximum 1000 characters).',
        }
        widgets = {
            'user_name': forms.TextInput(attrs={'placeholder': 'Your Name', 'minlength': 5}),
            'user_email': forms.EmailInput(attrs={'placeholder': 'Your Email'}),
            'message': forms.Textarea(attrs={
                'placeholder': 'Your Message',
                'rows': 5,
                'maxlength': 1000
            }),
        }  

    # Custom email validation
    def clean_email(self):
        email = self.cleaned_data.get('user_email')
        if '@example.com' in email:  # Restrict email domain as an example
            raise forms.ValidationError("We do not accept feedback from example.com addresses.")
        return email
            
