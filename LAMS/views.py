from django.shortcuts import render
from timetable.models import Labs

def index(request):
    lab = Labs.objects.count()
    return render(request, 'hello.html', {'lab': lab})
