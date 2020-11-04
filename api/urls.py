from django.urls import include, path
from rest_framework.routers import DefaultRouter

from users.urls import users_router

from .views import (CategoriesViewSet, CommentViewSet, GenreViewSet,
                    ReviewViewSet, TitleViewSet)

v1_router = DefaultRouter()
v1_router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)
v1_router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)
v1_router.register('titles', TitleViewSet, basename=TitleViewSet)
v1_router.register('categories', CategoriesViewSet, basename=CategoriesViewSet)
v1_router.register('genres', GenreViewSet, basename=GenreViewSet)
v1_router.register('categories/<slug:slug>', CategoriesViewSet, basename=CategoriesViewSet)
v1_router.register('genres/<slug:slug>', GenreViewSet, basename=GenreViewSet)

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/auth/', include('users.urls')),
    path('v1/users/', include(users_router.urls)),
]
