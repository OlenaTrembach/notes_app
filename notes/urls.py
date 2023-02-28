from django.contrib import admin
from django.urls import path
from notes.views import My_notes, NotesFormView, get_topic_list, delete_topic

urlpatterns = [
    path('list', My_notes),
    path('form', NotesFormView.as_view()),
    path('notes_list/', get_topic_list),
    path('delete/', delete_topic),
]