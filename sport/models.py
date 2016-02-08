# -*- coding: utf-8 -*-

from django.db import models


class Typeofmeasure(models.Model):
    name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name.encode('utf-8')


class Discipline(models.Model):
    name = models.CharField(max_length=100, blank=True)
    typeofmeasure = models.ForeignKey('Typeofmeasure', on_delete=models.CASCADE)

    def __str__(self):
        return self.name.encode('utf-8')


class Competition(models.Model):
    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=100)
    event_date = models.DateField(default='2016-01-01')
    discipline = models.ForeignKey(Discipline)
    distance = models.DecimalField(max_digits=8, decimal_places=4, default=0)
    notes = models.TextField(max_length=1000, null=True)  # location, time, fee

    score = models.DurationField(default='00:00')

    def __str__(self):
        return self.name.encode('utf-8')

    def distance_without_zeros(self):
        return ('%f' % self.distance).rstrip('0').rstrip('.')
