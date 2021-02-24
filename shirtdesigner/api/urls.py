from django.urls import path
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
# from shirtdesigner.api.views import(
#     MenuListView,
#     FabricListView,
# )
from shirtdesigner.api.views import *

app_name = 'shirtdesigner'

urlpatterns = [
    path('sidebar/', MenuListView.as_view(), name="sidebar"),
    path('fabric/', FabricListView.as_view(), name='fabric'),
    path('silhouette/', SilhouetteListView.as_view(), name='silhouette'),
    path('sleeve/', SleeveListView.as_view(), name='sleeve'),
    path('placket/', PlacketListView.as_view(), name='placket'),
    path('collar/', CollarListView.as_view(), name='collar'),
    path('cuff/', CuffListView.as_view(), name='cuff'),
    path('pocket/', PocketListView.as_view(), name='pocket'),
    path('test/', api_detail_blog_view, name='test'),
]