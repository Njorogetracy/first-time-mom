from django.views.generic import ListView, TemplateView
from .models import Activity, Booking
# from .forms import CustomUserCreationForm
# from django.contrib.auth import login
# from django.shortcuts import render, redirect
# from allauth.account.views import SignupView, LoginView, LogoutView
# from .login import CustomLoginForm
# from django.urls import reverse_lazy


class IndexView(TemplateView):
    template_name = 'index.html'


class HubView(TemplateView):
    template_name = 'home.html'


class ActivityListView(ListView):
    model = Activity
    template_name = 'activity_list.html'
    context_object_name = 'activities'


# class CustomSignupView(SignupView):
#     model = CustomUser
#     form_class = CustomUserCreationForm
#     template_name = 'accounts/custom_signup.html'
#     success_url = reverse_lazy('login')

#     def form_valid(self, form):
#         user = form.save()
#         login(self.request, user)
#         return super().form_valid(form)


# class CustomLoginView(LoginView):
#     form_class = CustomLoginForm
#     template_name = 'accounts/login.html'
#     success_url = reverse_lazy('home')

#     def form_valid(self, form):
#         user = form.get_user()
#         login(self.request, user)
#         return super().form_valid(form)


# class CustomLogoutView(LogoutView):
#     template_name = 'accounts/logout.html'
