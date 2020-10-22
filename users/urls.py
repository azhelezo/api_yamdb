from django.urls import include, path
from rest_framework.routers import SimpleRouter

from users import views

from .views import UserViewSet

users_router = SimpleRouter()
users_router.register('', UserViewSet, basename='users')

urlpatterns = [
    path('email/', views.signup, name='signup'),
    path('token/', views.login, name='login'),
]
