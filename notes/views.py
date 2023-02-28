from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render, redirect
from django.views.generic import FormView

from notes.models import Notes
from notes.forms import NotesForm


def My_notes(request):
    my_notes = Notes.objects.filter(author_id=request.user.id)
    context = {'my2': my_notes}
    return render(request, 'profile.html', context)


def get_topic_list(request):
    topic_type = request.GET.get('type', None)
    if topic_type:
        queryset = Notes.objects.filter(type=topic_type, author_id=request.user.id)
    else:
        queryset = Notes.objects.filter(author_id=request.user.id)
    context = {'my2': queryset}
    return render(request, 'profile.html', context)


def create_notes_form(request):
    if request.method == 'POST':
        print(request.POST.get("title"))
        form = NotesForm(request.POST)
        if form.is_valid():
            # Topic.objects.create(**form.cleaned_data)
            return redirect('my2')
    else:
        form = NotesForm()
        return render(request, 'form.html', {'form': form})


def delete_topic(request):
    # I
    my_id = request.GET.get('my_id', None)
    topic = Notes.objects.get(id=my_id)
    topic.delete()
    # II
    # Topic.objects.filter(id=4).delete()
    return render(request, 'profile.html', {'my2': Notes.objects.filter(author_id=request.user.id)})


class NotesFormView(FormView):
    template_name = 'form.html'
    form_class = NotesForm
    success_url = 'list'

    def form_valid(self, form):
        Notes.objects.create(**form.cleaned_data)
        return HttpResponseRedirect(self.get_success_url())

# def index(request):
#     return HttpResponse("Hello from Notes app")
