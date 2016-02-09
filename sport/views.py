import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.template.context_processors import csrf
from .forms import CompetitionForm, DisciplineForm
from .models import Competition, Discipline


@login_required
def competition_list(request):
    competitions = Competition.objects.order_by('event_date').filter(author=request.user)
    return render(request, 'sport/competition_list.html', {

        'competitions': competitions
    })


@login_required
def comp_detail(request, pk):
    comp = get_object_or_404(Competition, pk=pk)
    return render(request, 'sport/comp_detail.html', {'comp': comp})


@login_required
def competition_new(request):
    if request.method == "POST":
        form = CompetitionForm(request.POST)
        if form.is_valid():
            comp = form.save(commit=False)
            comp.author = request.user
            comp.save()
            return redirect('comp_detail', pk=comp.pk)
    else:
        form = CompetitionForm()
    return render(request, 'sport/comp_edit.html', {'form': form})


@login_required
def discipline_new(request):
    if request.method == "POST":
        form = DisciplineForm(request.POST)
        if form.is_valid():
            comp = form.save(commit=False)
            comp.save()
            return redirect('disciplines')
    else:
        form = DisciplineForm()
    return render(request, 'sport/discipline_new.html', {'form': form})


@login_required
def comp_edit(request, pk):
    comp = get_object_or_404(Competition, pk=pk)
    if request.method == "POST":
        form = CompetitionForm(request.POST, instance=comp)
        if form.is_valid():
            comp = form.save(commit=False)
            comp.author = request.user
            comp.save()
            return redirect('comp_detail', pk=comp.pk)
    else:
        form = CompetitionForm(instance=comp)
    return render(request, 'sport/comp_edit.html', {'form': form})


@login_required
def comp_remove(request, pk):
    comp = get_object_or_404(Competition, pk=pk)
    comp.delete()
    return redirect('sport.views.competition_list')


@login_required
def upcoming_events(request):
    competitions = Competition.objects.order_by('event_date').filter(author=request.user).filter(
            event_date__gte=datetime.datetime.now())
    return render(request, 'sport/competition_list.html', {

        'competitions': competitions
    })


@login_required
def events_from_date(request, lower):
    if lower == "True":
        competitions = Competition.objects.order_by('event_date').filter(author=request.user).filter(
                event_date__lt=datetime.datetime.now())
    else:
        competitions = Competition.objects.order_by('event_date').filter(author=request.user).filter(
                event_date__gte=datetime.datetime.now())

    return render(request, 'sport/competition_list.html', {

        'competitions': competitions
    })


@login_required
def sorted_view(request, field):
    competitions = Competition.objects.order_by(field, 'event_date').filter(author=request.user)

    return render(request, 'sport/competition_list.html', {

        'competitions': competitions
    })


@login_required
def filtered_view_discipline(request, field):
    competitions = Competition.objects.order_by('event_date').filter(author=request.user, discipline__name=field)

    return render(request, 'sport/competition_list.html', {

        'competitions': competitions
    })


@login_required
def comp_list_for_dist(request, dist, disc):
    competitions = Competition.objects.order_by('event_date').filter(author=request.user).filter(
            distance=dist, discipline__name=disc)
    return render(request, 'sport/statistics_for_specific_dist.html', {

        'competitions': competitions
    })


@login_required
def statistics(request):  # , year, month):
    disciplines = Discipline.objects.all()

    return render(request, 'sport/disciplines_list.html', {

        'disciplines': disciplines
    })


@login_required
def disciplines(request):
    disciplines = Discipline.objects.all()

    return render(request, 'sport/disciplines.html', {

        'disciplines': disciplines
    })


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register/complete')

    else:
        form = UserCreationForm()
    token = {}
    token.update(csrf(request))
    token['form'] = form

    return render_to_response('registration/registration_form.html', token)


def registration_complete(request):
    return render_to_response('registration/registration_complete.html')


def comp_list_for_discipline(request, disc):
    distances = list(Competition.objects
                     .filter(author=request.user, discipline__name=disc).order_by()
                     .values_list('distance', flat=True).distinct())

    distances.sort()
    dist_dict = {}
    for dist in distances:
        dist_dict[dist] = Competition.objects.filter(author=request.user, distance=dist, discipline__name=disc)

    competitions = dist_dict
    return render(request, 'sport/statistics.html', {

        'competitions': competitions
    })


def summary(request):
    disciplines_list = Discipline.objects.all()
    disciplines_dict = {}
    for disc in disciplines_list:
        activities_counter = len(Competition.objects.filter(author=request.user, discipline__name=disc,
                                                            event_date__lt=datetime.datetime.now()))
        overall_distance = Competition.objects.filter(author=request.user, discipline__name=disc,
                                                      event_date__lt=datetime.datetime.now()).aggregate(
                Sum('distance'))
        overall_time = Competition.objects.filter(author=request.user, discipline__name=disc,
                                                  event_date__lt=datetime.datetime.now()).aggregate(Sum('score'))
        if activities_counter > 0:
            disciplines_dict[disc] = [activities_counter, _get_distance(overall_distance['distance__sum']),
                                    _get_time(overall_time['score__sum'])]

    return render(request, 'sport/summary.html', {

        'disciplines_dict': disciplines_dict
    })


def _get_distance(dist):
    if dist is None:
        return 0
    return ('%f' % dist).rstrip('0').rstrip('.')


def _get_time(time):
    if time is None:
        return 0
    return time
