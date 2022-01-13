from rest_framework import serializers, exceptions

from .models import StaticItem


class StaticSerializer(serializers.ModelSerializer):
    cpc = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    cpm = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = StaticItem
        fields = '__all__'

    def validate(self, attrs):
        if attrs.get('views', 0) <= 0:
            attrs['views'] = None
        if attrs.get('click', 0) <= 0:
            attrs['click'] = None
        if 'cost' in attrs and attrs['cost'] < 0:
            raise exceptions.ValidationError('cost must be positive')

        return attrs