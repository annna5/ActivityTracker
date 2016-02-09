### Anna Gawłowska  

# Activity-Tracker - Dokumentacja techniczna

Projekt został napisany w Pythonie 2.7.9, przy użyciu frameworku Django w wersji 1.9.2.  
Wykorzystałam m.in. biblioteki sqlite3, django.db, django.forms, django.models, pakiet datetime.

### Struktura projektu:
```
ActivityTracker
├
├── db.sqlite3
├── manage.py
├── mysite
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
└── sport
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── __init__.py
    ├── migrations
    │   ├── 0001_initial.py
    │   ├── __init__.py
    ├── models.py
    ├── static
    │   └── css
    │       └── sport.css
    ├── templates
    │   ├── registration
    │   │   ├── login.html
    │   │   ├── registration_complete.html
    │   │   └── registration_form.html
    │   └── sport
    │       ├── base.html
    │       ├── calendar.html
    │       ├── comp_detail.html
    │       ├── comp_edit.html
    │       ├── competition_list.html
    │       ├── discipline_new.html
    │       ├── disciplines.html
    │       ├── disciplines_list.html
    │       ├── statistics_dist_list.html
    │       ├── statistics_for_specific_dist.html
    │       ├── statistics.html
    │       └── summary.html
    ├── urls.py
    ├── views.py
```
### Opis przykładowych funkcji z pliku `views.py`:
- *events_from_date(request, lower)*
```python
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
```    
##### objaśnienie:
Argument `lower` może przyjmować wartości `true` (gdy chcemy wybrać daty z przeszłości) lub `false` (gdy chcemy wybrać daty z przyszłości).  
Do zmiennej `competitions` przypisujemy posortowane po polu `event_date` (`.order_by('event_date')`) te obiekty klasy 
`Competittions,` których autorem jest użytkownik wysyłający zapytanie  (`.filter(author=request.user)`)
i których pole `event_date` jest mniejsze (`lt`) / większe lub równe (`gte`) niż aktualna data (`datetime.datetime.now()`).  
Listę `competitions` przekazujemy razem z zapytaniem `request` do szablonu `competition_list.html`. 
- *comp_list_for_discipline(request, disc)*
```python
def comp_list_for_discipline(request, disc):
    distances = list(Competition.objects
                     .filter(author=request.user, discipline__name=disc)
                     .values_list('distance', flat=True).distinct())
    distances.sort()
    dist_dict = {}
    for dist in distances:
        dist_dict[dist] = Competition.objects.filter(author=request.user, distance=dist, discipline__name=disc)
    competitions = dist_dict
    return render(request, 'sport/statistics.html', {
        'competitions': competitions
    })
```
##### objaśnienie:
Celem tej funkcji jest przekazanie do szablonu listy aktywności dla konkretnej dyscypliny.  
Do zmiennej `distances` przypisujemy listę bez powtórzeń dystansów (`.values_list('distance', flat=True).distinct())`) obiektów klasy `Competition`, 
których nazwa dyscypliny (`discipline__name`) jest równa przekazanej jako argument zmiennej `dist`.  
Uzyskaną listę sortujemy(`distances.sort()`).  
Tworzony jest słownik  `dist_dict`,
którego kluczami są dystanse z utworzonej wcześniej listy a wartościami lista obiektów klasy `Competition,` z odpowiednim autorem, dystansem i dyscypliną.  
- *summary(request)*
```python
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
```
##### objaśnienie:

Funkcja tworzy słownik, którego kluczami są dyscypliny, w których użykownik ma zapisaną co najmniej jedną aktywność  
(`if activities_counter > 0`), a wartościami lista zawierająca liczbę aktywności, łączny dystans i łączny czas pokonany 
przez użytkownika w danej dyscyplinie.  
Suma dystasu i czasu jest obliczana za pomącą funkcji agregującej `Sum`.  
Dodatkowo wykorzystywane są pomocnicze funkcje `get_distance()` i `get_time()` odpowiednio formatujące wartości: 

```python
def _get_distance(dist):
    if dist is None:
        return 0
    return ('%f' % dist).rstrip('0').rstrip('.')
    
def _get_time(time):
    if time is None:
        return 0
    return time
```
 

