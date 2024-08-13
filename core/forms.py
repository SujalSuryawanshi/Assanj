from django import forms
from .models import Staller,Rating, MenuItems, FooRating,Foo_Category, New_offer
from django import forms
from rest_framework import serializers
from users.models import CustomUser

class SignInForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    phone = forms.CharField(max_length=15, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput, required=True)
    class Meta:
        model = CustomUser
        fields = ['username', 'phone', 'password', 'confirm_password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match")

        return cleaned_data
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if CustomUser.objects.filter(phone=phone).exists():
            raise forms.ValidationError("A user with this phone number already exists.")
        return phone


class StallerForm(forms.ModelForm):
    class Meta:
        model = Staller
        fields = [
           'address', 'category', 'video', 'contact',
            'timings', 'keywords'
        ]


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rating']
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),
        }


class AddItemForm(forms.ModelForm):
    class Meta:
        model = MenuItems
        fields = ['menu_photo', 'name', 'foo_cat', 'normal_price', 'premium_price','description']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)




class MenuRatingForm(forms.ModelForm):
    class Meta:
        model = FooRating
        fields = ['rating']
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),
        }


class FooCategoryForm(forms.ModelForm):
    class Meta:
        model = Foo_Category
        fields = ['foo_name'] 

class NewOfferForm(forms.ModelForm):
    class Meta:
        model=New_offer
        fields=['title','offer_photo','message']

class EditOfferForm(forms.ModelForm):
    class Meta:
        model = New_offer
        fields = ['title', 'offer_photo', 'message']
