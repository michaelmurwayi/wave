from django.urls import path, include
from .views import HomeView, DonateView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('donate/', DonateView.as_view(), name="donate")
]