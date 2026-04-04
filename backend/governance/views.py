from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Proposal, Vote
from .serializers import ProposalSerializer,VoteSerializer

@api_view(['GET'])
def get_proposals(request):
    proposals = Proposal.objects.all()
    serializer = ProposalSerializer(proposals, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def cast_vote(request):
    serializer = VoteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)