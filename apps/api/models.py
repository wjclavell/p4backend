from django.db import models
from apps.authentication.models import User

# Create your models here.
class Game(models.Model):
    event_id = models.CharField(max_length=255, default="")   # event_id from 'rundown'
    sport = models.IntegerField(null=True)    # id number from 'rundown' ie: 3 = MLB, 2 = NFL
    team1 = models.CharField(max_length=100)    # team names
    team2 = models.CharField(max_length=100)
    score1 = models.IntegerField(default=0)    # team scores
    score2 = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.sport}: {self.team1} v. {self.team2}'


class Bid(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)   # associate a bid with its user
    game = models.ForeignKey(Game, on_delete=models.DO_NOTHING)   # associate a bid with specific game
    event_id = models.CharField(max_length=255, default="")   # used to find real life game associated with this bid
    amount = models.IntegerField()    # how much the user bids
    team = models.CharField(max_length=100)    # user's choice of who will win
    result = models.CharField(max_length=10, blank=True,null=True)    # updated based on result of game (Win/Lose)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.amount} | {self.team}'
