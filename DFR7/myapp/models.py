from django.db import models

# Create your models here.c
class Author(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField( max_length=50)
    subject=models.CharField( max_length=50)


    def __str__(self):
        return  self.first_name

class Book(models.Model):
    title=models.CharField(max_length=50)
    author=models.ForeignKey(Author,on_delete=models.CASCADE,related_name='books_by_author')
    release=models.DateField(auto_now=False, auto_now_add=False)
    rating=models.IntegerField()

    def __str__(self):
        return self.title

  

