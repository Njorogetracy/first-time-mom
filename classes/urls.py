from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),  # for users not registered
    path('hub/', HubView.as_view(), name='hub'),  # homepage for loggedin
    path('activities/', ActivityListView.as_view(), name='activity_list'),
]
