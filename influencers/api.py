import json

from django.http import HttpResponse
from rest_framework import viewsets, permissions, views
from .serializers import InstagramUserSerializer
from rest_framework.response import Response
from rest_framework import filters

from influencers.models import InstagramUser
from influencers.utils import get_user


# Influencer Viewset
class InfluencerViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.AllowAny
    ]

    queryset = InstagramUser.objects.all()

    serializer_class = InstagramUserSerializer

    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['followers', 'engagement']

def getProfileInsights(request, username):
    user = get_user(username)
    return HttpResponse(json.dumps(user))
