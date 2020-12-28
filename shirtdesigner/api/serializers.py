from rest_framework import serializers
from shirtdesigner.models import SubSideBarModel, SideBarModel, StyleSideBarModel, FabricModel

import os
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.storage import FileSystemStorage

class SubSideSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubSideBarModel
        fields = '__all__'

class MenuSerializer(serializers.ModelSerializer):
    sub_bar = SubSideSerializer(many=True)
    class Meta:
        model = SideBarModel
        fields = [
            'icon',
            'title_ru', 'title_en', 'title_uz',
            'url',
            'sub_stat',
            'sub_bar',
            'search_stat',
            'search_url',
            'related_menu_stat',
        ]


class FabricSerializer(serializers.ModelSerializer):
    class Meta:
        model = FabricModel
        fields = '__all__'
