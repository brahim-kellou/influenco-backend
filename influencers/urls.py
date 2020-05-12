from rest_framework import routers
from django.urls import path, include
from .api import InfluencerViewSet, getProfileInsights

router = routers.DefaultRouter()
router.register('api/influencers', InfluencerViewSet, 'influencers')

urlpatterns = [
    path('', include(router.urls)),
    path('api/profile/<username>', getProfileInsights)
]
