from rest_framework import serializers

from users.models import User

from . import models
from .models import Categories, Genre, Title


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'bio', 'email', 'role', ]
        extra_kwargs = {
            'first_name': {'required': False},
            'last_name': {'required': False},
            'bio': {'required': False},
            }


class GenreSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = ('name', 'slug')
        model = Genre
        lookup_field = 'slug'


class CategoriesSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = ('name', 'slug')
        model = Categories
        lookup_field = 'slug'


class TitleViewSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True, read_only=True)
    category = CategoriesSerializer(read_only=True)

    class Meta:
        fields = '__all__'
        model = Title


class TitlePostSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(slug_field='slug', many=True, queryset=Genre.objects.all())
    category = serializers.SlugRelatedField(slug_field='slug', queryset=Categories.objects.all())

    class Meta:
        fields = '__all__'
        model = Title


class TitleSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Titles
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    title = serializers.SlugRelatedField(
        slug_field='name',
        read_only=True,
    )

    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
    )

    class Meta:
        model = models.Review
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    review = serializers.SlugRelatedField(
        slug_field='text',
        read_only=True
    )
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = models.Comment
        fields = '__all__'
