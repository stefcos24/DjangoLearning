from django import views
from django.urls import path
from .views import HomeView, TeacherCreateView, ThankYou, ContactFormView, TeacherListView, TeacherDetailView

app_name = 'classroom'

urlpatterns = [
    path('', HomeView.as_view(), name='home_view'),
    path('thank_you/', ThankYou.as_view(), name='thank_you'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('create_teacher/', TeacherCreateView.as_view(), name='create_teacher'),
    path('list_teacher/', TeacherListView.as_view(), name='list_teacher'),
    path('teacher_detail/<int:pk>', TeacherDetailView.as_view(), name='detail_teacher')
]