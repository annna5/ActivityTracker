from django import forms

from .models import Competition, Discipline


class CompetitionForm(forms.ModelForm):
    class Meta:
        model = Competition
        error_css_class = 'error'
        required_css_class = 'required'
        fields = ('name', 'discipline', 'distance', 'score', 'event_date', 'notes')


class DisciplineForm(forms.ModelForm):
    class Meta:
        model = Discipline
        error_css_class = 'error'
        required_css_class = 'required'
        fields = ('name', 'typeofmeasure')
