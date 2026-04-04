from django.contrib import admin
from .models import User, Proposal, Vote

# Register your models here.
admin.site.register(User)
admin.site.register(Proposal)
admin.site.register(Vote)
