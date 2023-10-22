from django.db import transaction
from django.db.models import F
from django.views.generic import ListView, TemplateView, FormView, CreateView  # noqa
from django.db.models import Avg
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import Activity, Booking, Review
from .forms import BookingForm, ReviewForm


class IndexView(TemplateView):
    template_name = 'index.html'


class HubView(TemplateView):
    template_name = 'home.html'


class ActivityListView(ListView):
    model = Activity
    template_name = 'activity_list.html'
    context_object_name = 'activities'

    def get_queryset(self):
        return Activity.objects.annotate(average_rating=Avg('review__rating'))


class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'review.html'
    success_url = 'activity_list'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.approved = True
        form.instance.activity = Activity.objects.get(pk=self.kwargs['activity_id'])  # noqa
        return super().form_valid(form)


class ReviewListView(ListView):
    model = Review
    template_name = 'review.html'
    context_object_name = 'review'

    def get_queryset(self):
        activity_id = self.kwargs['activity_id']
        return Review.objects.filter(activity_id=activity_id, approved=False)


class BookingView(FormView):
    model = Booking
    form_class = BookingForm
    template_name = 'booking.html'

    def form_valid(self, form):
        activity = Activity.objects.get(pk=self.kwargs['activity_id'])
        user = self.request.user
        email = user.email
        num_bookings = Booking.objects.filter(activity=activity,
                                              is_confirmed=True).count()
        max_participants = activity.max_participants

        if num_bookings < max_participants:
            booking = Booking(user=user, activity=activity)
            booking.is_confirmed = True
            booking.save()
            num_bookings += 1
            activity.current_num_of_participants = num_bookings
            activity.save()

            booked_activities = Booking.objects.filter(user=user, is_confirmed=True)  # noqa

            if num_bookings < max_participants:
                return render(self.request, 'booking-confirmation.html', {'booked_activities': booked_activities})  # noqa
            else:
                return render(self.request,
                              'fully_booked.html', {'activity': activity})
        else:
            return render(self.request,
                          'fully_booked.html', {'activity': activity})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['activity'] = Activity.objects.get(pk=self.kwargs['activity_id'])  # noqa
        user = self.request.user
        email = user.email
        context['booked_activities'] = Booking.objects.filter(user=user, is_confirmed=True)  # noqa
        return context


class BookingConfirmationView(TemplateView):
    template_name = 'confirmation.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['confirmation_message'] = "Your booking was successful!"
        return context


class BookingListView(ListView):
    model = Booking
    template_name = 'booking_list.html'
    context_object_name = 'bookings'


class UserBookedActivitiesView(ListView):
    model = Booking
    template_name = 'user_booked_activities.html'
    context_object_name = 'user_booked_activities'

    def get_queryset(self):
        user = self.request.user
        email = user.email
        return Booking.objects.filter(user=user, is_confirmed=True)