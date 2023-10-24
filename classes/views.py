from django.views.generic import ListView, TemplateView, FormView, CreateView
from django.views.generic.detail import DetailView
from django.views import View
from django.db.models import Avg
from django.shortcuts import redirect, render, get_object_or_404
from .models import Activity, Booking, Review
from .forms import BookingForm, ReviewForm


class IndexView(TemplateView):
    template_name = 'index.html'


class HubView(TemplateView):
    template_name = 'home.html'


class ActivityListView(ListView):
    model = Activity
    template_name = 'activity_list.html'
    paginate_by = 5
    context_object_name = 'activities'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for activity in context['activities']:
            activity.reviews = activity.review_set.all()
            activity.avg_rating = activity.reviews.aggregate(Avg('rating'))['rating__avg']   # noqa
        return context


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
        return Review.objects.filter(activity_id=activity_id, approved=True)


class BookingView(FormView):
    model = Booking
    form_class = BookingForm
    template_name = 'booking.html'

    def form_valid(self, form):
        activity = Activity.objects.get(pk=self.kwargs['activity_id'])
        user = self.request.user
        email = user.email

        existing_booking = Booking.objects.filter(user=user,
                                                  activity=activity,
                                                  is_confirmed=True).first()
        if existing_booking:
            return render(self.request, 
                          'already_booked.html', {'activity': activity})

        booking = form.save(commit=False)
        booking.user = user
        booking.activity = activity
        booking.save()

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
                return render(self.request, 'confirmation.html', {'booked_activities': booked_activities})  # noqa
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


class BookingConfirmationView(View):
    template_name = 'confirmation.html'

    def get(self, request, booking_id):
        booking = Booking.objects.get(pk=booking_id)
        activity = booking.activity
        user = booking.user

        context = {
            'booking': booking,
            'activity': activity,
            'user': user,
        }

        return render(request, self.template_name, context)


class UserBookedActivitiesView(View):
    template_name = 'user_booked_activities.html'

    def get(self, request):
        user = request.user
        email = user.email
        bookings = Booking.objects.filter(user=user, is_confirmed=True)
        context = {
            'bookings': bookings,
        }
        return render(request, self.template_name, context)


class BookingCancellationConfirmationView(TemplateView):
    template_name = 'cancel_confirmation.html'

    def get_context_data(self, **kwargs):
        booking = get_object_or_404(Booking,
                                    pk=self.kwargs['booking_id'],
                                    user=self.request.user, is_confirmed=True)
        return {'booking': booking}


class BookingCancellationView(DetailView):
    model = Booking
    template_name = 'cancel_confirmation.html'

    def get_object(self, queryset=None):
        return get_object_or_404(
            Booking, pk=self.kwargs['booking_id'],
            user=self.request.user, is_confirmed=True)

    def post(self, request, *args, **kwargs):
        booking = self.get_object()
        booking.is_confirmed = False
        booking.save()
        return redirect('user_booked_activities')