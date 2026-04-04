from rest_framework import serializers
from .models import Proposal,Vote

class ProposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposal
        fields = '__all__'
    
class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'