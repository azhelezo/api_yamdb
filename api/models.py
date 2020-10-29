from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    searh_fields = ['slug']
    
    class Meta:
        ordering = ['-id']

class Categories(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    searh_fields = ['slug']

    class Meta:
        ordering = ['-id']

class Title(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField(blank=True, null=True)
    description = models.TextField()
    genre = models.ManyToManyField(Genre, blank=True)
    category = models.ForeignKey(
        Categories,
        on_delete=models.PROTECT,
        related_name='category',
        blank=True
    )

    class Meta:
        ordering = ['-id']

