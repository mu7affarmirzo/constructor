from django.contrib import admin
from modeltranslation.admin import TranslationAdmin


from .models import *

admin.site.register(FabricModel)
admin.site.register(StyleTypeModel)
# admin.site.register(SleeveTypeModel)
admin.site.register(ShirtSleeveModel)
# admin.site.register(YokeTypeModel)
admin.site.register(YokeModel)
# admin.site.register(ShoulderTypeModel)
# admin.site.register(ShoulderModel)
# admin.site.register(BackDetailsTypeModel)
admin.site.register(BackDetailsModel)
# admin.site.register(BottomCutTypeModel)
admin.site.register(BottomCutModel)
# admin.site.register(CollarTypeModel)
admin.site.register(CollarModel)
# admin.site.register(CuffTypeModel)
# admin.site.register(PlacketTypeModel)
admin.site.register(CuffModel)
admin.site.register(PlacketModel)
admin.site.register(PocketModel)
# admin.site.register(CollarButtonModel)
# admin.site.register(CuffButtonModel)
# admin.site.register(PlacketButtonModel)
# admin.site.register(CollarThreadModel)
# admin.site.register(CuffThreadModel)
# admin.site.register(PlacketThreadModel)

# class SideBarCustomAdmin(admin.ModelAdmin):
#     list_display = ('title_ru')

class SideBarCustomAdmin(admin.ModelAdmin):
    list_display = ('title_ru', 'title_en', 'title_uz',)

class SideBarAdmin(SideBarCustomAdmin, TranslationAdmin):
    pass
admin.site.register(SideBarModel, SideBarAdmin)

class SubSideBarAdmin(TranslationAdmin):
    pass
admin.site.register(SubSideBarModel, SubSideBarAdmin)

class StyleSideBarAdmin(TranslationAdmin):
    pass
admin.site.register(StyleSideBarModel, StyleSideBarAdmin)