from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.CreateProfile.as_view(), name='register'),
]
