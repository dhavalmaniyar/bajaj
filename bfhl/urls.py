from django.urls import path
from .views import View

urlpatterns = [
    path('bfhl', View.as_view(), name='view'),
]