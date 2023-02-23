from django.contrib import admin
from django.urls import path
from notes.views import My_notes

urlpatterns = [
    path('', My_notes),
]