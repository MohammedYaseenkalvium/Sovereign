from django.contrib import admin
from .models import Team,User, Proposal, Vote

# Register your models here.
admin.site.register(Team)
admin.site.register(User)
admin.site.register(Proposal)
admin.site.register(Vote)
