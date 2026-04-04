from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Proposal(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    deadline = models.DateTimeField()
    status = models.CharField(max_length=20, default='active')

    def __str__(self):
        return self.title

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    proposal = models.ForeignKey(Proposal, on_delete=models.CASCADE)
    vote = models.BooleanField() 

    class Meta:
        unique_together = ('user', 'proposal')