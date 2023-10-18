from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('hub/', HubView.as_view(), name='hub'),
    path('activities/', ActivityListView.as_view(), name='activity_list'),
    # path('accounts/signup/', CustomSignupView.as_view(), name='signup'),
    # path('accounts/login/', CustomLoginView.as_view(), name='login'),
    # path('accounts/logout/', CustomLogoutView.as_view(), name='logout'),
]
