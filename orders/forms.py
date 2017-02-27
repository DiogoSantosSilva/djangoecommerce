from django import forms
from django.contrib.auth import get_user_model
from .models import UserAdress

User =  get_user_model()

class GuestCheckoutForm(forms.Form):
    email = forms.EmailField()
    email2 = forms.EmailField(label='Verify Email')

    def clean_email2(self):
        email = self.cleaned_data.get("email")
        email2 = self.cleaned_data.get("email2")

        if email == email2:
            user_exists = User.objects.filter(email=email).count()
            if user_exists != 0:
                raise forms.ValidationError("User exist please login")
            return email2
        else:
            raise forms.ValidationError("Please confirm emails are the same")

class AddressForm(forms.Form):
    billing_address = forms.ModelChoiceField(
        queryset=UserAdress.objects.filter(type="billing"),
        empty_label = None
        )
    shipping_address = forms.ModelChoiceField(
        queryset=UserAdress.objects.filter(type="shipping"),
        empty_label = None,
        )


class UserAddressForm(forms.ModelForm):
    class Meta:
        model = UserAdress
        fields = [
            'street',
            'city',
            'state',
            'zipcode',
            'type',
        ]
