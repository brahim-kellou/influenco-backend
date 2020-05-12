from influencers.models import Influencer
from rest_framework import viewsets, permissions
from .serializers import InfluencerSerializer


# Influencer Viewset
class InfluencerViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.AllowAny
    ]

    queryset = Influencer.objects.all()

    serializer_class = InfluencerSerializer
