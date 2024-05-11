from django.urls import path
from ..test_views import test

urlpatterns = [
    path('', test, name='test'),
]