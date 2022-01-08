from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('live_view', views.live_view, name = 'live'),
]