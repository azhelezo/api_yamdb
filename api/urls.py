from django.urls import include, path

from users.urls import users_router
from .views import view_self
from rest_framework.routers import DefaultRouter
from .views import TitleViewSet, CategoriesViewSet, GenreViewSet

v1_router = DefaultRouter()

v1_router.register('titles', TitleViewSet, basename=TitleViewSet)
v1_router.register('categories', CategoriesViewSet, basename=CategoriesViewSet)
v1_router.register('genres', GenreViewSet, basename=GenreViewSet)
v1_router.register('categories/<slug:slug>', CategoriesViewSet, basename=CategoriesViewSet)
v1_router.register('genres/<slug:slug>', GenreViewSet, basename=GenreViewSet)

urlpatterns = [
    path('v1/auth/', include('users.urls')),
    path('v1/users/me/', view_self),
    path('v1/users/', include(users_router.urls)),
    path('v1/', include(v1_router.urls))
]
