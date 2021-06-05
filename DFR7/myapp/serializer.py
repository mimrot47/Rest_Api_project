from rest_framework import serializers
from .models import Author , Book 

class Bookseri(serializers.ModelSerializer):

    class Meta:
        model= Book 
        fields='__all__'

class Authorseri(serializers.ModelSerializer):
    Books_by_author=Bookseri(read_only=True,many=True)
    class Meta:
        model=Author 
        fields='__all__'