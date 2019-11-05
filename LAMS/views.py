from django.shortcuts import render


def index(request):
    return_dict = dict()
    return_dict['total_weeks'] = range(1, 20)
    return render(request, 'index.html', return_dict)
