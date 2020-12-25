from django.urls import path
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from shirtdesigner.api.views import(
    MenuListView,
    FabricListView,
)

app_name = 'shirtdesigner'

urlpatterns = [
    path('sidebar/', MenuListView.as_view(), name="sidebar"),
    path('fabric/', FabricListView.as_view(), name='fabric'),
]