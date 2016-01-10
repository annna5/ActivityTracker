from django.shortcuts import render, get_object_or_404, redirect
from .models import Competition
from .forms import CompetitionForm
from django.contrib.auth.decorators import login_required


@login_required
def competition_list(request):
    competitions = Competition.objects.order_by('event_date')
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
            # post.author = request.user
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
            # comp.author = request.user
            # comp.published_date = timezone.now()
            comp.save()
            return redirect('comp_detail', pk=comp.pk)
    else:
        form = CompetitionForm(instance=comp)
    return render(request, 'sport/comp_edit.html', {'form': form})
