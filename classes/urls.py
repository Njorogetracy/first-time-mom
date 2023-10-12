from django.urls import path
from .views import ActivityListView, IndexView, HubView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('hub/', HubView.as_view(), name='hub'),
    path('activities/', ActivityListView.as_view(), name='activity_list'),
]
