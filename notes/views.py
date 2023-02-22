from django.http import HttpResponse

from django.shortcuts import render



def index(request):
    my_dict = [
        {
            'title': 'First Post',
            'content': 'This is my first blog post'
        },
        {
            'title': 'Second Post',
            'content': 'This is my second blog post'
        },
        {
            'title': 'Third Post',
            'content': 'This is my third blog post'
        }
    ]
    context = {'my2': my_dict}
    return render(request, 'profile.html', context)

# def index(request):
#     return HttpResponse("Hello from Notes app")
