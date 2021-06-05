from django.contrib import admin
from .models import Author,Book

# Register your models her
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','subject']

class BookAdmin(admin.ModelAdmin):
    list_display = ['title','author','release','rating']

admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)
