from rest_framework import serializers
from influencers.models import Influencer

# Influencer Serializer


class InfluencerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Influencer
        fields = '__all__'
