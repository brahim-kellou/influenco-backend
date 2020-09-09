from rest_framework import serializers
from influencers.models import InstagramUser

# Influencer Serializer


class InstagramUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstagramUser
        fields = '__all__'
