from django.shortcuts import render
from timetable.models import Labs

def index(request):
    lab = Labs.objects.count()
    return render(request, 'manage.html', {'lab': lab})
