# from django import forms
# from .models import Shop

# class ShopForm(forms.ModelForm):
#     class Meta:
#         model = Shop
#         fields = ["name", "address", "category", "latitude", "longitude"]


# from django import forms
# from .models import Shop

# class ShopForm(forms.ModelForm):
#     class Meta:
#         model = Shop
#         fields = ['name', 'address', 'category', 'latitude', 'longitude']

#         widgets = {
#             'name': forms.TextInput(attrs={'class': 'form-control'}),
#             'address': forms.TextInput(attrs={'class': 'form-control'}),
#             'category': forms.Select(attrs={'class': 'form-select'}),
#             'latitude': forms.NumberInput(attrs={'class': 'form-control'}),
#             'longitude': forms.NumberInput(attrs={'class': 'form-control'}),
#         }


from django import forms
from .models import Shop

class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        
        # EXCLUDE owner so users cannot modify it
        fields = ['name', 'address', 'category', 'latitude', 'longitude']
        
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter shop name'
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter full address'
            }),
            # If category has choices in model, this will automatically render correctly
            'category': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'E.g., Medical, Restaurant, Clothing'
            }),
            'latitude': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.000001',
                'placeholder': 'Click on map to auto-fill'
            }),
            'longitude': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.000001',
                'placeholder': 'Click on map to auto-fill'
            }),
        }

from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter username"
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Enter password"
        })
    )

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomSignupForm(UserCreationForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Enter password"
        })
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Confirm password"
        })
    )

    class Meta:
        model = User
        fields = ["username", "email"]

        widgets = {
            "username": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter username"
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Enter email"
            }),
        }
