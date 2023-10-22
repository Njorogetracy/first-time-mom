from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),  # for users not registered
    path('hub/', HubView.as_view(), name='hub'),  # homepage for loggedin
    path('activities/', ActivityListView.as_view(), name='activity_list'),
    path('activity/<int:activity_id>/review/create',
         ReviewCreateView.as_view(), name='create_review'),
    path('activity/<int:activity_id>/review/',
         ReviewListView.as_view(), name='activity_review'),
    path('book/<int:activity_id>/',
         BookingView.as_view(), name='book_activity'),
    path('book/booking-confirmation/',
         BookingConfirmationView.as_view(), name='booking-confirmation'),
    path('bookings/', BookingListView.as_view(), name='booking_list'),
    path('user_booked_activities/',
         UserBookedActivitiesView.as_view(), name='user_booked_activities'),
]
