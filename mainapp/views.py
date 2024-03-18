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
    print(serializer)
    return Response(serializer.data)


@api_view(['GET'])
def goods(request):
    token = TokenSerializer(data={'token': request.GET.get('token')})
    if token.is_valid(raise_exception=True):
        goods_list = Goods.objects.all()
        serializer = GoodsSerializer(goods_list, many=True)
        return Response(serializer.data)
    return HttpResponse(token.errors, status=401)

class NewGoods(APIView):
    def post(self, request):
        new_goods = GoodsSerializer(data=request.data)
        if new_goods.is_valid():
            print(new_goods)
            new_goods.save()
            return HttpResponse("Success<br>Goods id: " + str(new_goods.instance.id))
        else:
            return Response(new_goods.errors, status=400)
