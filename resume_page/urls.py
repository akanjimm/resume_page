from django.urls import path
from resume_page import views

urlpatterns = [
    path('', views.resume_view, name='resume'),
]