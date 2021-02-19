from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
# from rest_framework.filters import SearchFilter, OrderingFilter

from shirtdesigner.models import *
from shirtdesigner.api.serializers import (
    MenuSerializer,
    FabricSerializer,
    SiluetSerializer,
    SleeveSerializer,
PlacketSerializer,
CollarSerializer,
CuffSerializer,
PocketSerializer
)

class PocketListView(ListAPIView):
    queryset = PocketStyleModel.objects.all()
    serializer_class = PocketSerializer
    pagination_class = PageNumberPagination

class CuffListView(ListAPIView):
    queryset = CuffStyleModel.objects.all()
    serializer_class = CuffSerializer
    pagination_class = PageNumberPagination

class CollarListView(ListAPIView):
    queryset = CollarStyleModel.objects.all()
    serializer_class = CollarSerializer
    pagination_class = PageNumberPagination

class PlacketListView(ListAPIView):
    queryset = PlacketStyleModel.objects.all()
    serializer_class = PlacketSerializer
    pagination_class = PageNumberPagination

class SleeveListView(ListAPIView):
    queryset = SleeveStyleModel.objects.all()
    serializer_class = SleeveSerializer
    pagination_class = PageNumberPagination


class MenuListView(ListAPIView):
    queryset = SideBarModel.objects.all()
    serializer_class = MenuSerializer
    pagination_class = PageNumberPagination
    # filter_backends = (SearchFilter, OrderingFilter)
    # search_fields = ('title', 'body', 'author__username')

class FabricListView(ListAPIView):
    queryset = FabricModel.objects.all()
    serializer_class = FabricSerializer
    pagination_class = PageNumberPagination
    # filter_backends = (SearchFilter, OrderingFilter)
    # search_fields = ('title', 'body', 'author__username')


class SilhouetteListView(ListAPIView):
    queryset = SiluetStyleModel.objects.all()
    serializer_class = SiluetSerializer
    pagination_class = PageNumberPagination