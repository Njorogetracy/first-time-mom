from django.views.generic import ListView, TemplateView, FormView
from .models import Activity, Booking
from .forms import BookingForm


class IndexView(TemplateView):
    template_name = 'index.html'


class HubView(TemplateView):
    template_name = 'home.html'


class ActivityListView(ListView):
    model = Activity
    template_name = 'activity_list.html'
    context_object_name = 'activities'


class BookingView(FormView):
    form_class = BookingForm
    template_name = 'booking.html'
    success_url = 'thank-you'