from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Review, Booking
from django.core.exceptions import ValidationError
from datetime import date

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


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']


class BookingForm(forms.ModelForm):
    due_date = forms.DateField(required=True, label='date',
                               widget=forms.TextInput(attrs={'type': 'date'}))
    has_journal = forms.BooleanField(required=True,
                                     label="Do you have a journal?")
    needs_journal = forms.BooleanField(required=True,
                                       label="Do you need a journal?")

    def clean_due_date(self):
        data = self.cleaned_data['due_date']
        if data < date.today():
            raise forms.ValidationError('Booking date cannot be in the past')
        else:
            print(f"Valid due_date selected: {data}")
        return data

    class Meta:
        model = Booking
        fields = ['has_journal', 'needs_journal', 'due_date']