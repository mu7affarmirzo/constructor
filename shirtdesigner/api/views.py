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

    # x = CollarObjModel.objects.all()
    # print(x)

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




@api_view(['GET', ])
def api_detail_blog_view(request):


    if request.method == "GET":
        x = CollarObjModel.objects.all()
        a = CollarObjModel.objects.values()
        # a = x.filter(style_collar='Pointed collar')
        # print(x[0].style_collar)
        print(a['style_collar_id'=="2"])
        # b = a.filter(style_collar_id=2)
        b = a.filter(style_collar_id=2, fabric_id=90)
        return Response(b)

# @api_view(['POST',])
# @permission_classes((IsAuthenticated,))
# def api_manipulate_view(request):
#
#     if request.method == "POST":
#         serializer = BlogPostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)