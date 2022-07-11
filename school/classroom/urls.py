from django import views
from django.urls import path
from .views import HomeView, ThankYou

app_name = 'classroom'

urlpatterns = [
    path('', HomeView.as_view(), name='home_view'),
    path('thank_you/', ThankYou.as_view(), name='thank_you')
]