from rest_framework import routers
from .api import InfluencerViewSet

router = routers.DefaultRouter()
router.register('api/influencers', InfluencerViewSet, 'influencers')

urlpatterns = router.urls
