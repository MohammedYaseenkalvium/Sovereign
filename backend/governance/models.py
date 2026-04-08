from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class User(models.Model):
    
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=20)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='members', null=True, blank=True)

    def __str__(self):
        return self.name

class Proposal(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    deadline = models.DateTimeField()
    status = models.CharField(max_length=20, default='active')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    proposal = models.ForeignKey(Proposal, on_delete=models.CASCADE)
    vote = models.BooleanField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'proposal'], name='unique_user_proposal')
        ]