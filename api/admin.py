from django.contrib import admin

from .models import Comment, Review, Title, Category, Genre


class TitleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'year', 'genre', 'category')
    search_fields = ('title', 'year')
    empty_value_display = '-пусто-'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'category', 'slug')
    search_fields = ('category', 'slug')
    empty_value_display = '-пусто-'


class GenreAdmin(admin.ModelAdmin):
    list_display = ('pk', 'genre', 'slug')
    search_fields = ('genre', 'slug')
    empty_value_display = '-пусто-'


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'author', 'text')
    search_fields = ('title', 'author', 'text')
    empty_value_display = '-пусто-'


class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'review', 'author', 'text')
    search_fields = ('review', 'author', 'text')
    empty_value_display = '-пусто-'

admin.site.register(Title, TitleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)
