from django.http import HttpResponse

from django.shortcuts import render

from notes.models import Notes


def My_notes(request):
    my_notes = Notes.objects.all()
    context = {'my2': my_notes}
    return render(request, 'profile.html', context)

# def index(request):
#     return HttpResponse("Hello from Notes app")
