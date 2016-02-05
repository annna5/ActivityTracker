from django.db import models
from django.contrib import admin


class Student(models.Model):
    name = models.CharField(max_length=100)
    nr_index = models.CharField(max_length=100)


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)


class Book(models.Model):
    title = models.CharField(max_length=100)
    length = models.IntegerField()
    author = models.ForeignKey('Author', related_name = 'books')


class Person(models.Model):
    id_number = models.CharField(max_length=10, primary_key=True, unique=True)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)


class NewPerson(models.Model):
    first = models.CharField(max_length=100)
    middle = models.CharField(max_length=100, blank=True)
    last = models.CharField(max_length=100)

    class Meta:
        ordering = ['last', 'first', 'middle']
        unique_together = ['first', 'last', 'middle']
        verbose_name_plural = 'people'



class Journal(models.Model):
    title = models.CharField(max_length=100)

class Article(models.Model):
    headline = models.CharField(max_length=100)
    journals = models.ManyToManyField(Journal, related_name = 'articles')

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name','nr_index')

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title','length')

class PersonAdmin(admin.ModelAdmin):
    list_display = ('id_number','first_name','last_name')

class JournalAdmin(admin.ModelAdmin):
    list_display = ('title',)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('headline',)

class NewPersonAdmin(admin.ModelAdmin):
    list_display = ('first','middle','last')

admin.site.register(Book, BookAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Journal, JournalAdmin)
admin.site.register(NewPerson, NewPersonAdmin)
admin.site.register(Student, StudentAdmin)
