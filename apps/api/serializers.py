from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import Game, Bid


class BidSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Bid
        fields = ('id', 'event_id', 'game', 'owner', 'amount', 'team', 'result', 'created_at', 'updated_at')


class GameSerializer(serializers.ModelSerializer):
    bids = BidSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Game
        fields = ('id', 'event_id', 'bids', 'sport', 'team1', 'team2', 'score1', 'score2', 'created_at', 'updated_at')
