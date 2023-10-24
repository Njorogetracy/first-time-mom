from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),  # for users not registered
    path('hub/', HubView.as_view(), name='hub'),  # homepage for loggedin
    path('activities/', ActivityListView.as_view(), name='activity_list'),
    path('book/<int:activity_id>/',
         BookingView.as_view(), name='book_activity'),
    path('book/<int:booking_id>/booking-confirmation/',
         BookingConfirmationView.as_view(), name='booking-confirmation'),
    path('user_booked_activities/',
         UserBookedActivitiesView.as_view(), name='user_booked_activities'),
    path('book/<int:booking_id>/cancel/',
         BookingCancellationView.as_view(), name='cancel-booking'),
    path('book/<int:booking_id>/cancel/confirmation/',
         BookingCancellationConfirmationView.as_view(),
         name='cancel_confirmation'),
    path('activity/<int:activity_id>/review/create',
         ReviewCreateView.as_view(), name='create_review'),
    path('activity/<int:activity_id>/review/',
         ReviewListView.as_view(), name='activity_review'),
    path('activity/<int:activity_id>/all_reviews/',
         AllReviewsListView.as_view(), name='all_reviews'),
]
