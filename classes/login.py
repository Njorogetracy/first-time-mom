# from django import forms
# from django.contrib.auth.forms import AuthenticationForm
# from allauth.account.forms import LoginForm
# from django.contrib.auth import get_user_model


# class CustomLoginForm(AuthenticationForm):
#     # email = forms.EmailField(
#     #     label='Email',
#     #     widget=forms.TextInput(attrs={'autofocus': True})
#     # )
#     # password = forms.CharField(
#     #     label='Password',
#     #     strip=False,
#     #     widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}),
#     # )

#     def clean(self):
#         cleaned_data = super().clean()
#         email = cleaned_data.get('email')
#         password = cleaned_data.get('password')

#         user = get_user_model().objects.filter(email=email).first()
#         if not user:
#             raise forms.ValidationError('Invalid email or password.')

#         if not user.check_password(password):
#             raise forms.ValidationError('Invalid email or password.')

#         return cleaned_data
