import json

from django.http import HttpResponse
from rest_framework import viewsets, permissions, views
from .serializers import InfluencerSerializer
from rest_framework.response import Response

from influencers.models import Influencer
from influencers.utils import get_user


# Influencer Viewset
class InfluencerViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.AllowAny
    ]

    queryset = Influencer.objects.all()

    serializer_class = InfluencerSerializer


def getProfileInsights(request, username):
    user = get_user(username)
    return HttpResponse(json.dumps(user))
