from django.db import models


class Genre(models.Model):
    genre = models.CharField("Genre", max_length=100)
    slug = models.SlugField(blank=False, unique=True)

class Category(models.Model):
    category = models.CharField("Genre", max_length=100)
    slug = models.SlugField(blank=False, unique=True)
    
       
class Titles(models.Model):
    name = models.CharField("Title", max_length=200)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    year = models.DateTimeField("Release date", auto_now_add=True, db_index=True)

#class GenreTitle(models.Model):
#    title_id = models.IntegerField()
#    genre_id = models.IntegerField()



