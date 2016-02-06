import datetime
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.template.context_processors import csrf
from django.utils.safestring import mark_safe

from sport.utils.Calendar import Calendar
from .models import Competition, Discipline
from .forms import CompetitionForm
from django.contrib.auth.decorators import login_required


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
            # post.published_date = timezone.now()
            comp.save()
            return redirect('comp_detail', pk=comp.pk)
    else:
        form = CompetitionForm()
    return render(request, 'sport/comp_edit.html', {'form': form})


@login_required
def comp_edit(request, pk):
    comp = get_object_or_404(Competition, pk=pk)
    if request.method == "POST":
        form = CompetitionForm(request.POST, instance=comp)
        if form.is_valid():
            comp = form.save(commit=False)
            comp.author = request.user
            # comp.published_date = timezone.now()
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
def comp_list_for_dist(request, dist):
    competitions = Competition.objects.order_by('event_date').filter(author=request.user).filter(
            distance=dist)
    return render(request, 'sport/statistics_for_specific_dist.html', {

        'competitions': competitions
    })


# @login_required
# def calendar(request):  # , year, month):
#     activities = Competition.objects.order_by('event_date').filter(
#             event_date__year=2016, event_date__month=1
#     )
#     cal = Calendar(activities).formatmonth(2016, 1)
#     return render_to_response('sport/calendar.html', {'calendar': mark_safe(cal),})

@login_required
def calendar(request):  # , year, month):
    disciplines = Discipline.objects.all()

    return render(request, 'sport/disciplines_list.html', {

        'disciplines': disciplines
    })


@login_required
def statistics(request):
    distances = list(Competition.objects
                     .filter(author=request.user).order_by()
                     .values_list('distance', flat=True).distinct())
    distances.sort()
    dist_dict = {}
    for dist in distances:
        dist_dict[dist] = Competition.objects.filter(author=request.user).filter(distance=dist)

    competitions = dist_dict
    return render(request, 'sport/statistics.html', {

        'competitions': competitions
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
