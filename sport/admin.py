from django.contrib import admin
from .models import Competition, Discipline, Typeofmeasure #, Result

admin.site.register(Competition)
admin.site.register(Discipline)
admin.site.register(Typeofmeasure)
# admin.site.register(Result)


