from django.contrib import admin

from .models import Question, Vocabulary
# Register your models here.

admin.site.register(Question) #tell the admin that Question objects have an admin interface
admin.site.register(Vocabulary) #tell the admin that Vocabulary objects have an admin interface