from django import forms
from notes.models import Notes


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        exclude = ('reminder',)
