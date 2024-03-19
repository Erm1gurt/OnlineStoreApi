from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from mainapp.models import Tokens, Goods
from mainapp.serializers import TokenSerializer, GoodsSerializer


# Create your views here.

@api_view(['GET'])
def get_token(request):
    new_token = Tokens()
    new_token.create_token()
    serializer = TokenSerializer(new_token)
    return Response(serializer.data)


@api_view(['GET'])
def goods(request):
    token = TokenSerializer(data={'token': request.GET.get('token', None)})
    if token.is_valid():
        goods_list = Goods.objects.all()
        serializer = GoodsSerializer(goods_list, many=True)
        return Response(serializer.data)
    return HttpResponse(token.errors['token'], status=401)


class NewGoods(APIView):
    def get(self, request):
        token = TokenSerializer(data={'token': request.GET.get('token', None)})
        if token.is_valid():
            return Response(status=200)

        return HttpResponse(token.errors['token'], status=401)

    def post(self, request):
        new_goods = GoodsSerializer(data=request.data)
        if new_goods.is_valid():
            new_goods.save()
            return HttpResponse("Success<br>Goods id: " + str(new_goods.instance.id), status=201)
        else:
            return Response(new_goods.errors, status=400)
