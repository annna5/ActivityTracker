from django.shortcuts import render
from .models import Competition


def competition_list(request):
    competitions = Competition.objects.order_by('event_date')
    return render(request, 'sport/competition_list.html', {

        'competitions':competitions
    })
