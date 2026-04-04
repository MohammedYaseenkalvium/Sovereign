from django.urls import path
from .views import cast_vote, get_proposals

urlpatterns = [
    path('proposals/', get_proposals, name='get_proposals'),
    path('vote/',cast_vote, name='cast_vote'),
]