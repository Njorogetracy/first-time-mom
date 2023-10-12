from django.urls import path
from .views import ActivityListView, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('activities/', ActivityListView.as_view(), name='activity_list'),
]
