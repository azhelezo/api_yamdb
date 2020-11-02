from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import UserViewSet, login, signup

users_router = SimpleRouter()
users_router.register('', UserViewSet, basename='users')

urlpatterns = [
    path('email/', signup, name='signup'),
    path('token/', login, name='login'),
]
