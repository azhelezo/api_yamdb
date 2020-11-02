from django.db.models import Avg
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, mixins, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .filters import CategoriesFilter, GenresFilter, TitlesFilter
from .models import Category, Genre, Review, Title
from .permissions import IsAdminOrReadOnly, ReviewCommentPermission
from .serializers import (CategoriesSerializer, CommentSerializer,
                          GenreSerializer, ReviewSerializer,
                          TitlePostSerializer, TitleViewSerializer)


class CreateListDestroyViewSet(mixins.CreateModelMixin,
                               mixins.DestroyModelMixin,
                               mixins.ListModelMixin,
                               viewsets.GenericViewSet):
    pass


class GenreViewSet(CreateListDestroyViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()
    pagination_class = PageNumberPagination
    permission_classes = (IsAuthenticatedOrReadOnly, IsAdminOrReadOnly)
    filter_backends = [filters.SearchFilter]
    filterset_class = GenresFilter
    search_fields = ('name', 'slug')
    lookup_field = 'slug'


class CategoriesViewSet(CreateListDestroyViewSet):
    serializer_class = CategoriesSerializer
    queryset = Category.objects.all()
    pagination_class = PageNumberPagination
    permission_classes = (IsAuthenticatedOrReadOnly, IsAdminOrReadOnly)
    filter_backends = [filters.SearchFilter]
    filterset_class = CategoriesFilter
    search_fields = ('name', 'slug')
    lookup_field = 'slug'


class TitleViewSet(viewsets.ModelViewSet):
    serializer_class = TitlePostSerializer
    queryset = Title.objects.all()
    pagination_class = PageNumberPagination
    permission_classes = (IsAuthenticatedOrReadOnly, IsAdminOrReadOnly)
    filter_backends = [DjangoFilterBackend]
    filterset_class = TitlesFilter
    search_fields = ('name', 'year')

    def get_serializer_class(self):
        if self.action == 'retrieve' or self.action == 'list':
            return TitleViewSerializer
        return TitlePostSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.rating = instance.reviews.all().aggregate(Avg('score'))['score__avg']
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [ReviewCommentPermission]

    def get_queryset(self):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        return title.reviews.all()

    def perform_create(self, serializer):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        if title.reviews.filter(author=self.request.user).exists():
            raise ValidationError(detail='Only one review is allowed')
        serializer.save(title=title, author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [ReviewCommentPermission]

    def get_queryset(self):
        review = get_object_or_404(
            Review,
            pk=self.kwargs.get('review_id')
        )
        return review.comments.all()

    def perform_create(self, serializer):
        review = get_object_or_404(
            Review,
            pk=self.kwargs.get('review_id')
        )
        serializer.save(review=review, author=self.request.user)
