### Anna Gawłowska

 

# Activity-Tracker - Dokumentacja użytkownika 
 

### Instrukcja uruchomienia w systemie Linux:

Do uruchomienia projektu niezbędny jest zainstalowany Python w wersji 2.7.9 oraz Django w wersji co najmniej 1.8

#### Instalacja/aktualizacja Django:
- Należy zainstalować program pip (instalator pakietów i narzędzi do Pythona):
```python
sudo apt-get install python-pip
```
- w przypadku braku zainstalowanego django należy wykonać polecenie:
```python
sudo pip install Django
```

- jeśli Django jest zainstalowane sprawdzamy jego wersję:
```python
django-admin –-version
```
- jeżeli mamy wersję starszą niż 1.8, możemy ją uaktualnić poleceniem:
```python
sudo pip install -U Django
```
#### Uruchomienie aplikacji
- Po rozpakowaniu archiwum ActivityTracker.zip należy przejść do katalogu ActiivityTracker i wykonać komendę:
```python
python manage.py runserver
```
- następnie uruchomić w przeglądarce localserver pod adresem wskazanym w konsoli (http://127.0.0.1:8000/)

#### Utworzenie konta
- W prawym panelu strony startowej niezalogowany użytkownik może zalogować się lub utworzyć konto.
- Można utworzyć nowe konto albo skorzystać z testowego użytkownika zawierającego już wpisy w bazie danych (login: *Alice* hasło: *django5django*)
- Strona startowa zalogowanego użytkownika zawiera listę zapisanych aktywności (jeśli jakiekolwiek istnieją).

#### Możliwe przypadki użycia:
- Dodawanie nowej aktywności:
znak plusa w prawym panelu

- Wyświetlenie szczegółów aktywności:
w dowolnym widoku zawierającym listę aktywności, kliknięcie w nazwę aktywności spowoduje przeniesienie do podstrony ze szczegółami aktywności

- Edycja, usuwanie aktywności:
w widoku szczegółów aktywności w można edytować (ikona ołówka po prawej stronie) i usuwać (znak X po prawej stronie)

- Podgląd podsumowania aktywności
sumaryczne dane o zakończonych aktywnościach są dostępne pod ikoną listy po prawej stronie

- Widoki:
  - Dla konkretnej dyscypliny: Zakładka *disciplines* wyświetla wszystkie aktywności w wybranej dyscyplinie, oraz umożliwia dodanie nowej dyscypliny.

  - Dla konkretnej dyscypliny i wybranego dystansu: zakładka *statistics* umożliwia wyświetlenie aktywności w wybranej dyscyplinie i na konkretnym dystansie.

  - Dwie ostatnie zakładki to lista zaplanowanych aktywności oraz lista aktywności, które już miały miejsce. 

- Sortowanie:
pod zakładką *Home* dostępna jest lista wszystkich aktywności. Kliknięcie na nazwę kolumny spowoduje posortowanie listy według daty, nazwy, dystansu, czasu trwania.
