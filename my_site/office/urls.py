from django.urls import path
from . import views

# domain.com/office ---> list of all patient
urlpatterns = [
    path('', views.list_patient, name='list_patient')
]