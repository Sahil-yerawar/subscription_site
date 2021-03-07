# serializers.py

from rest_framework import serializers
from .models import Subscriptions

class SubscriptionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subscriptions
        fields = ('email',)
