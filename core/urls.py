from django.urls import path
from .views import public_api, protected_api, register_user

urlpatterns = [
    path('public/', public_api),
    path('protected/', protected_api),
    path('register/', register_user),
]
