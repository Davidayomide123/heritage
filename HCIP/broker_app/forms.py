from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import UserProfile  # Import your UserProfile model

class CreateUserForm(UserCreationForm):
    firstname = forms.CharField(max_length=10, required=True)
    lastname = forms.CharField(max_length=10, required=True)
    email = forms.EmailField(max_length=30, required=True)
    phonenumber = forms.CharField(max_length=10, required=True)
    
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('PNTS', 'Prefer not to say'),
    )
    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=True)
    
    STATUS_CHOICES = (
        ('Employed', 'Employed'),
        ('Unemployed', 'Unemployed'),
        ('Retired', 'Retired'),
        ('Disabled', 'Disabled'),
    )
    status = forms.ChoiceField(choices=STATUS_CHOICES, required=True)
    
    ACCOUNT_TYPE_CHOICES = (
        ('Online Account', 'Online Account'),
        ('Savings Account', 'Savings Account'),
        ('Fixed Account', 'Fixed Account'),
        ('Shared Account', 'Shared Account'),
    )
    account_type = forms.ChoiceField(choices=ACCOUNT_TYPE_CHOICES, required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'firstname', 'lastname', 'status', 'gender', 'account_type', 'phonenumber']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['firstname']
        user.last_name = self.cleaned_data['lastname']
        user.email = self.cleaned_data['email']
        
        if commit:
            user.save()
        
        # Create or update UserProfile
        profile, created = UserProfile.objects.get_or_create(user=user)
        profile.phonenumber = self.cleaned_data['phonenumber']
        profile.gender = self.cleaned_data['gender']
        profile.status = self.cleaned_data['status']
        profile.account_type = self.cleaned_data['account_type']
        profile.save()
        
        return user



class DepositForm(forms.Form):
    deposit_amount = forms.DecimalField(max_digits=10, decimal_places=2)

    def __init__(self, *args, **kwargs):
        self.user_profile = kwargs.pop('user_profile', None)
        super().__init__(*args, **kwargs)

    def clean_deposit_amount(self):
        deposit_amount = self.cleaned_data['deposit_amount']

        if deposit_amount <= 0:
            raise forms.ValidationError("Amount must be greater than zero.")

        if deposit_amount > self.user_profile.balance:
            raise forms.ValidationError(f"You cannot withdraw more than your current balance ({self.user_profile.balance}).")

        min_deposit_amount = 10  # Example minimum deposit amount
        if deposit_amount < min_deposit_amount:
            raise forms.ValidationError(f"Minimum withdraw amount required is {min_deposit_amount}.")

        return deposit_amount

    def save(self):
        if self.is_valid():
            deposit_amount = self.cleaned_data['deposit_amount']
            # Perform actions to process the deposit (if needed)
            return deposit_amount  # Return the deposit amount if processing is successful
        else:
            raise ValueError("Form is not valid, cannot save.")
