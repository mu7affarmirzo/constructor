from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
# from rest_framework.filters import SearchFilter, OrderingFilter

from shirtdesigner.models import SideBarModel
from shirtdesigner.api.serializers import MenuSerializer

class MenuListView(ListAPIView):
    queryset = SideBarModel.objects.all()
    serializer_class = MenuSerializer
    pagination_class = PageNumberPagination
    # filter_backends = (SearchFilter, OrderingFilter)
    # search_fields = ('title', 'body', 'author__username')