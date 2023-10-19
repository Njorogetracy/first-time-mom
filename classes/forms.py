from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Booking


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True,
                                 help_text="Required. Enter your first name.")
    last_name = forms.CharField(max_length=30, required=True,
                                help_text="Required. Enter your last name.")

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name')


class BookingForm(forms.ModelForm):
    due_date = forms.DateField(required=False,
                               widget=forms.TextInput(attrs={'type': 'date'}))
    has_journal = forms.BooleanField(required=False,
                                     label="Do you have a journal?")
    needs_journal = forms.BooleanField(required=False,
                                       label="Do you need a journal?")

    class Meta:
        model = Booking
        fields = ['has_journal', 'needs_journal', 'due_date']
