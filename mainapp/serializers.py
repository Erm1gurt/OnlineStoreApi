from rest_framework import serializers
from mainapp.models import Goods, Tokens


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tokens
        fields = ['token']

    def validate(self, data):
        if not data['token']:
            return serializers.ValidationError('Token must be present')

        if not Tokens.objects.filter(token=data['token']).all():
            return serializers.ValidationError('Token is invalid')

        return data

class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = ['name', 'amount', 'price']

    def validate(self, data):
        if not data['name']:
            raise serializers.ValidationError('The title cannot be empty')

        if data['amount'] < 1:
            raise serializers.ValidationError('Amount must be more than 0')

        if data['price'] < 1:
            raise serializers.ValidationError('Price must be more than 0')

        return data