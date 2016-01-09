from django.shortcuts import render, get_object_or_404
from .models import Competition
from .forms import CompetitionForm


def competition_list(request):
    competitions = Competition.objects.order_by('event_date')
    return render(request, 'sport/competition_list.html', {

        'competitions':competitions
    })


def comp_detail(request, pk):
    comp = get_object_or_404(Competition, pk=pk)
    return render(request, 'sport/comp_detail.html', {'comp': comp})


def competition_new(request):
    form = CompetitionForm()
    return render(request, 'sport/comp_edit.html', {'form': form})