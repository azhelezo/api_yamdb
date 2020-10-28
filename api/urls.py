from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api import views
from users.urls import users_router

from .views import view_self

v1_router = DefaultRouter()
v1_router.register('titles', views.TitleViewSet)
v1_router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    views.ReviewViewSet,
    basename='reviews'
)
v1_router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    views.CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/auth/', include('users.urls')),
    path('v1/users/me/', view_self),
    path('v1/users/', include(users_router.urls))
]
