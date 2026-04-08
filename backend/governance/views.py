from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Proposal, User, Vote
from .serializers import ProposalSerializer,VoteSerializer
from rest_framework import IsAuthenticated


@api_view(['GET'])
def get_proposals(request):
    proposals = Proposal.objects.all()
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

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_proposals(request):
    user = request.user  # from JWT

    
    custom_user = User.objects.get(name=user.username)
    team = custom_user.team

    proposals = Proposal.objects.filter(team=team)
    serializer = ProposalSerializer(proposals, many=True)

    return Response(serializer.data)

@api_view(['POST'])
def create_proposal(request):
    serializer = ProposalSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

