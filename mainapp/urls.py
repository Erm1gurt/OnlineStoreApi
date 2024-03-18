from django.urls import path
from . import views

urlpatterns = [
    path('get_token', views.get_token),
    path('goods', views.goods),
    path('new_good', views.NewGoods.as_view())
]