from django.urls import path
from .views import get_proposals

urlpatterns = [
    path('proposals/', get_proposals, name='get_proposals'),
]