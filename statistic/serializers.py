from rest_framework import serializers

from .models import StaticItem


class StaticSerializer(serializers.ModelSerializer):
    cpc = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    cpm = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = StaticItem
        fields = '__all__'
