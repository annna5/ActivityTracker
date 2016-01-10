from django import forms
from .models import Competition


class CompetitionForm(forms.ModelForm):
    class Meta:
        model = Competition
        fields = ('name', 'event_date', 'event_time', 'location', 'discipline')
