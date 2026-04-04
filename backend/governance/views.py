from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Proposal
from .serializers import ProposalSerializer

@api_view(['GET'])
def get_proposals(request):
    proposals = Proposal.objects.all()
    serializer = ProposalSerializer(proposals, many=True)
    return Response(serializer.data)