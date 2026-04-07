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

@api_view(['GET'])
def get_proposal_results(request, proposal_id):
    votes = Vote.objects.filter(proposal_id=proposal_id)
    total_votes = votes.count()
    yes_votes = votes.filter(vote=True).count()
    no_votes = votes.filter(vote=False).count()
    return Response({
        'proposal_id': proposal_id,
        'total_votes': total_votes,
        'yes': yes_votes,
        'no': no_votes
    })