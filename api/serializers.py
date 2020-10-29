from rest_framework import serializers

from users.models import User
from .models import Title, Categories, Genre


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
