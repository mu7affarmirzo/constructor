from rest_framework import serializers

import os
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.storage import FileSystemStorage

from shirtdesigner.models import (
    SideBarModel,
    SubSideBarModel, StyleSideBarModel,
    FabricModel,
    SiluetStyleModel,
    SleeveStyleModel,
    CollarStyleModel,
    CuffStyleModel,
    PlacketStyleModel,
    PocketStyleModel,
    CustomShirt
)

class PocketSerializer(serializers.ModelSerializer):
    class Meta:
        model = PocketStyleModel
        fields = '__all__'

class CuffSerializer(serializers.ModelSerializer):
    class Meta:
        model = CuffStyleModel
        fields = '__all__'

class CollarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollarStyleModel
        fields = '__all__'

class PlacketSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlacketStyleModel
        fields = '__all__'

class SiluetSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiluetStyleModel
        fields = '__all__'

class SleeveSerializer(serializers.ModelSerializer):
    class Meta:
        model = SleeveStyleModel
        fields = '__all__'

class StyleSideBarSerializer(serializers.ModelSerializer):
    class Meta:
        model = StyleSideBarModel
        fields = '__all__'


class SubSideSerializer(serializers.ModelSerializer):
    # sub_side = StyleSideBarSerializer(many=True)
    class Meta:
        model = SubSideBarModel
        fields = [
            'icon',
            'title_ru', 'title_en', 'title_uz',
            'url',
            'sub_stat',
            # 'sub_bar',
            'search_stat',
            'search_url',
            # 'related_menu_stat',
            # 'sub_side'
        ]

class MenuSerializer(serializers.ModelSerializer):
    sub_list = SubSideSerializer(many=True)

    class Meta:
        model = SideBarModel
        fields = [
            'icon',
            'title_ru', 'title_en', 'title_uz',
            'url',
            'sub_stat',
            'sub_list',
            'search_stat',
            'search_url',
            'related_menu_stat',

        ]
        # depth = 2




class FabricSerializer(serializers.ModelSerializer):
    class Meta:
        model = FabricModel
        fields = '__all__'
