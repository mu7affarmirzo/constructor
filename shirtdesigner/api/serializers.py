from rest_framework import serializers
from shirtdesigner.models import SubSideBarModel, SideBarModel, StyleSideBarModel

import os
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.storage import FileSystemStorage

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = SideBarModel
        fields = [
            'icon',
            'title_ru', 'title_en', 'title_uz',
            'sub_stat',
            'search_url',
            'search_stat',
            'related_menu_stat',
        ]