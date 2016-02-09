### Anna Gawłowska  

# Activity-Tracker - Dokumentacja implementacyjna 
 

Projekt został stworzony w oparciu o wzorzec projektowy Model-View-Controller (nazywany w Django wzorcem Model-View-Template).
- Schemat projektu:

![alt text](https://github.com/annna5/ActivityTracker/blob/master/rys1.png)

 
- Model:  
zawarte w pliku `models.py` klasy reprezentują przechowywane w bazie danych obiekty.
![alt text](https://github.com/annna5/ActivityTracker/blob/master/rys2.png)

- Template (standardowo *View*):  
pliki *.html* zawarte w folderze *templates*, definiują sposób przedstawienia danych zwracanych przez funkcje z poprzednmiego punktu  
Szablon bazowy znajduje się w pliku `base.html`  
Zawiera bloki (*template*) `content` i `rightcontent`, które są wypełniane przez rozszerzające ten plik szablony.  

- View (standardowo: *Controller*):  
Funkcje zawarte w pliku `views.py` są łącznikiem pomiędzy bazą danych a szablonami *.html*. Na podstawie danych pobranych z bazy określają co ma być wyświetlone na stronie.

### Opis wybranych funkcji z pliku *views.py*:

```python
def sorted_view(request, field):
    competitions = Competition.objects.order_by(field, 'event_date').filter(author=request.user)
    return render(request, 'sport/competition_list.html', {
        'competitions': competitions
    })
```    
argumenty:  
`request` – zapytanie, na podstawie którego będzie wygenerowana odpowiedź   
`field` – nazwa pola z modelu `Competition`, według którego lista aktywności ma być sortowana  

zwraca:  
przekierowanie zapytania `request` do szablonu `competition_list.html` odpowiedzialnego za wyświetlanie listy aktywności, wraz z posortowaną listą aktywności

```python
def filtered_view_discipline(request, field):
    competitions = Competition.objects.order_by('event_date').filter(author=request.user, discipline__name=field)
    return render(request, 'sport/competition_list.html', {
        'competitions': competitions
    })
```
argumenty:  
`request` – zapytanie, na podstawie którego będzie wygenerowana odpowiedź  
`field` – nazwa dyscypliny (obiektu typu `Discipline`), z której lista aktywności ma być wyświetlona  

zwraca:  
przekierowanie zapytania `request` do szablonu `competition_list.html` odpowiedzialnego za wyświetlanie listy aktywności, wraz z przefiltrowaną listą aktywności

```python
def comp_list_for_dist(request, dist, disc):
    competitions = Competition.objects.order_by('event_date').filter(author=request.user).filter(
            distance=dist, discipline__name=disc)
    return render(request, 'sport/statistics_for_specific_dist.html', {
        'competitions': competitions
    })
```
argumenty:  
`request` – zapytanie, na podstawie którego będzie wygenerowana odpowiedź   
`dist` – dystans, dla którego mają być wyświetlone aktywności  
`disc` – nazwa dyscypliny (obiektu typu `Discipline`), z której lista aktywności ma być wyświetlona  

zwraca:  
przekierowanie zapytania `request` do szablonu `statistics_for_specific_dist.html` odpowiedzialnego za wyświetlanie listy aktywności, wraz z przefiltrowaną listą aktywności  


