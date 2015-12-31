# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Result(models.Model):
    score = models.IntegerField(blank=True)

    def __str__(self):
        return self.score


# class DistanceResult(Result):
#     score = models.IntegerField(default=0)


# class TimeResult(Result):
#     score = models.TimeField(default='00:00')

#
# class TypeOfMeasure(models.Model):
#     TIME, DISTANCE = range(2)


class Discipline(models.Model):
    name = models.CharField(max_length=100, blank=True)
    # type_of_measure = models.Field(TypeOfMeasure)
    # def __init__(self, name):
    #     models.Model.__init__(self)
    #     self.name = name

    def __str__(self):
        return self.name.encode('utf-8')
 

class Competition(models.Model):
    name = models.CharField(max_length=100)
    models.Field
    location = models.CharField(max_length=100)
    event_date = models.DateField()
    event_time = models.TimeField(default='08:00')
    discipline = models.ForeignKey(Discipline)
    # if discipline.type_of_measure == TypeOfMeasure.TIME:
    #     result = models.ForeignKey(TimeResult, blank=True, default='00:00')
    # else:
    #     result = models.ForeignKey(DistanceResult, blank=True, default=0)

    # result = models.ForeignKey(Result, default=0, null=True)
    result = models.IntegerField(blank=True, null=True)
    place = models.IntegerField(blank=True, null=True)
    numberOfParticipants = models.IntegerField(blank=True, null=True)
    personalNotes = models.TextField(blank=True, null=True)

    # def __init__(self, name, location, event_date, event_time):
    #     models.Model.__init__(self)
    #     self.name = name
    #     self.location = location
    #     self.event_date = event_date
    #     self.event_time = event_time
    #     self.save()

    def set_place(self, place):
        self.place = place
        self.save()

    def set_number_of_participants(self, numb):
        self.numberOfParticipants = numb
        self.save()

    def set_personal_notes(self, notes):
        self.personalNotes = notes
        self.save()

    def __str__(self):
        return self.name.encode('utf-8')