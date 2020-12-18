from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import *
# from .models import (
#     FabricModel,
#     StyleTypeModel,
#     SleeveTypeModel,
#     ShirtSleeveModel,
#     YokeTypeModel,
#     YokeModel,
#     ShoulderTypeModel,
#     ShoulderModel,
#     BackDetailsTypeModel,
#     BackDetailsModel,
#     BottomCutTypeModel,
#     BottomCutModel, CollarTypeModel,
#     CollarModel, CuffTypeModel, CuffModel, PlacketTypeModel, PlacketModel,
#     CollarButtonModel, CuffButtonModel, PlacketButtonModel,
#     CollarThreadModel, CuffThreadModel, PlacketThreadModel
#
# )
# Register your models here.

admin.site.register(FabricModel)
admin.site.register(StyleTypeModel)
admin.site.register(SleeveTypeModel)
admin.site.register(ShirtSleeveModel)
admin.site.register(YokeTypeModel)
admin.site.register(YokeModel)
admin.site.register(ShoulderTypeModel)
admin.site.register(ShoulderModel)
admin.site.register(BackDetailsTypeModel)
admin.site.register(BackDetailsModel)
admin.site.register(BottomCutTypeModel)
admin.site.register(BottomCutModel)
admin.site.register(CollarTypeModel)
admin.site.register(CollarModel)
admin.site.register(CuffTypeModel)
admin.site.register(CuffModel)
admin.site.register(PlacketTypeModel)
admin.site.register(PlacketModel)
admin.site.register(CollarButtonModel)
admin.site.register(CuffButtonModel)
admin.site.register(PlacketButtonModel)
admin.site.register(CollarThreadModel)
admin.site.register(CuffThreadModel)
admin.site.register(PlacketThreadModel)
# admin.site.register(SideBarModel)
# admin.site.register(SubSideBarModel)
# admin.site.register(StyleSideBarModel)

class SideBarAdmin(TranslationAdmin):
    pass
admin.site.register(SideBarModel, SideBarAdmin)

class SubSideBarAdmin(TranslationAdmin):
    pass
admin.site.register(SubSideBarModel, SubSideBarAdmin)

class StyleSideBarAdmin(TranslationAdmin):
    pass
admin.site.register(StyleSideBarModel, StyleSideBarAdmin)