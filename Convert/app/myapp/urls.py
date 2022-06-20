from django.urls import path
from .views import getik

urlpatterns = [
    path('', getik)
]