from django.urls import path
from .views import cast_vote, get_proposals, get_proposal_results,create_proposal

urlpatterns = [
    path('proposals/', get_proposals, name='get_proposals'),
    path('vote/',cast_vote, name='cast_vote'),
    path('results/<int:proposal_id>/', get_proposal_results, name='proposal_results'),
    path('create/',create_proposal),
]