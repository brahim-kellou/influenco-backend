import json

from django.http import HttpResponse
from rest_framework import viewsets, permissions, views
from .serializers import InstagramUserSerializer
from rest_framework.response import Response
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from influencers.models import InstagramUser
from influencers.utils import get_user


# Influencer Viewset
class InfluencerViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.AllowAny
    ]

    queryset = InstagramUser.objects.filter(class_influence="influencer") | InstagramUser.objects.filter(class_influence="micro-influencer") 
    serializer_class = InstagramUserSerializer

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = {
        'class_influence': ['exact'],
        'business_category_name': ['exact', 'contains'], 
        'followers': ['exact', 'gte', 'lte'],
        'posts': ['exact', 'gte', 'lte'], 
    }
    ordering_fields = ['followers', 'engagement']

def getProfileInsights(request, username):
    user = get_user(username)
    return HttpResponse(json.dumps(user))
