from django.contrib import admin
from django.urls import path
from customer import views

urlpatterns = [
    path('email/', views.index, name="index"),
    path('email_info/', views.email_info, name="email_info"),
]