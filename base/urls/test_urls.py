from django.urls import path
from ..views.test_views import test

urlpatterns = [
    path('', test, name='test'),
]