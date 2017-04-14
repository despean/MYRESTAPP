from rest_framework import serializers
from .models import Trending


class TrendsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Trending
        fields = '__all__'
