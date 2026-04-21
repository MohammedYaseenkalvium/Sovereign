from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Proposal, User, Vote
from .serializers import ProposalSerializer,VoteSerializer



@api_view(['GET'])
def get_proposals(request):
    user_id = request.GET.get('user')

    if not user_id:
        return Response({"error":"User ID is required"}, status=400)
    
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({"error":"User not found"}, status=404)
    
    proposals = Proposal.objects.filter(team=user.team)
    serializer = ProposalSerializer(proposals, many=True)

    return Response(serializer.data)

@api_view(['POST'])
def cast_vote(request):
    user_id = request.data.get('user')
    proposal_id = request.data.get('proposal')

    user = User.objects.get(id=user_id)
    proposal = Proposal.objects.get(id=proposal_id)

    # 🔥 SECURITY CHECK
    if user.team != proposal.team:
        return Response({"error": "User cannot vote on another team's proposal"}, status=403)

    serializer = VoteSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def get_proposals_results(request):
    votes = Vote.objects.filter(proposal_id = proposal_id)

    return Response({
        "proposal_id": proposal_id,
        "yes_votes": votes.filter(vote=True).count(),
        "no_votes": votes.filter(vote=False).count(),
        "total_votes": votes.count()
    })

@api_view(['POST'])
def create_proposal(request):
    if not request.data.get('team'):
        return Response({"error":"Team ID is required"}, status=400)
    serializer = ProposalSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
