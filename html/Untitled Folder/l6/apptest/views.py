#-*- coding: utf-8 -*-

from django.shortcuts import render
from django.template import loader, Context
from django.http import HttpResponse
from apptest.models import Author, Book, Article, Journal

def create(request):
    a1 = Author (id=None, name=u'Czechow')

    b1 = Book (id=None, title=u'Wiśniowy sad', length = 100)
    b2 = Book (id=None, title=u'Wujaszek Wania', length = 150)

    a1.save()

    a1.books.add(b1)
    a1.books.add(b2)

    t = loader.get_template("my_template.html")
    c = Context() #slownik z danymi dla templatea
    return HttpResponse(t.render(c))

def createmany(request):
    a1 = Journal (id=None, title=u'Gazeta Naukowa')
    a2 = Journal (id=None, title=u'Naukowiec polski')

    b1 = Article (id=None, headline=u'Najnowsze zdobycze nauki')
    b2 = Article (id=None, headline=u'Cudowne udowodnienie nowych twierdzeń')

    a1.save()
    a2.save()
    b1.save()
    b2.save()

    a1.articles.add(b1)
    a1.articles.add(b2)
    a2.articles.add(b1)
    a2.articles.add(b2)


    t = loader.get_template("my_template.html")
    c = Context() #slownik z danymi dla templatea
    return HttpResponse(t.render(c))

def wyszukaj(request):
    moje_rekordy = Journal.objects.filter(
      title__endswith=u'ki',
      articles__headline__startswith=u'Naj'
    ).distinct()
    ile = moje_rekordy.count()
    t = loader.get_template("nowy_template.html")
    c = Context({'journals':moje_rekordy, 'ile':ile}) #slownik z danymi dla templatea
    return HttpResponse(t.render(c))