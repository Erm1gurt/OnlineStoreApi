from rest_framework import serializers
from mainapp.models import Goods, Tokens


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tokens
        fields = ['token']
        extra_kwargs = {"token": {"error_messages": {"blank": "Token must be present"}}}

    def validate_token(self, value):
        if not Tokens.objects.filter(token=value).exists():
            raise serializers.ValidationError('Token is invalid')

        return value


class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = ['name', 'amount', 'price']

    def validate(self, data):
        if data['amount'] < 1:
            raise serializers.ValidationError('Amount must be more than 0')

        if data['price'] < 1:
            raise serializers.ValidationError('Price must be more than 0')

        return data
