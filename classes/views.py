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

    def form_valid(self, form):
        activity = Activity.objects.get(pk=self.kwargs['activity_id'])
        max_participants = activity.max_participants
        num_bookings = Booking.objects.filter(activity=activity,
                                              is_confirmed=True).count()

        if num_bookings < max_participants:
            return redirect('booking-confirmation')
        else:
            return render(self.request,
                          'fully_booked.html', {'activity': activity})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['activity'] = Activity.objects.get(pk=self.kwargs['activity_id'])  # noqa
        return context


class BookingConfirmationView(TemplateView):
    template_name = 'confirmation.html'
