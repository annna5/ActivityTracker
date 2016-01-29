# -*- coding: utf-8 -*-

from django.db import models

# class Result(models.Model):
#     score = models.IntegerField(blank=True, null=True)
#
#     def __str__(self):
#         return self.score



from django.utils import timezone


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
    notes = models.TextField(max_length=1000, null=True) # location, time, fee

    score = models.DurationField(default='00:00')

    # quantity_score = models.IntegerField(default=0)
    # time_score = models.TimeField(default='00:00')
    # distance_score = models.DecimalField(default=0, decimal_places=2, max_digits=10)

    # if discipline.type_of_measure == TypeOfMeasure.TIME:
    #     result = models.ForeignKey(TimeResult, blank=True, default='00:00')
    # else:
    #     result = models.ForeignKey(DistanceResult, blank=True, default=0)

    # result = models.ForeignKey(Result, default=0, null=True)



    # result = models.DurationField(default='00:00')
    # place = models.IntegerField(blank=True, null=True)
    # numberOfParticipants = models.IntegerField(blank=True, null=True)
    # personalNotes = models.TextField(blank=True, null=True)

    # def __init__(self, name, location, event_date, event_time):
    #     models.Model.__init__(self)
    #     self.name = name
    #     self.location = location
    #     self.event_date = event_date
    #     self.event_time = event_time
    #     self.save()

    # def set_place(self, place):
    #     self.place = place
    #     self.save()
    #
    # def set_number_of_participants(self, numb):
    #     self.numberOfParticipants = numb
    #     self.save()
    #
    # def set_personal_notes(self, notes):
    #     self.personalNotes = notes
    #     self.save()

    def __str__(self):
        return self.name.encode('utf-8')
