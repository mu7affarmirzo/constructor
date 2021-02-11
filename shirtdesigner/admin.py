from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import *

admin.site.register(FabricModel)
# admin.site.register(SideBarModel)
admin.site.register(StyleModel)
admin.site.register(SiluetStyleModel)
# admin.site.register(SiluetObjModel)

admin.site.register(PlacketStyleModel)
# admin.site.register(PlacketObjModel)

# admin.site.register(SleeveObjModel)
admin.site.register(SleeveStyleModel)
admin.site.register(CollarStyleModel)
# admin.site.register(CollarStiffnessModel)
# admin.site.register(CollarObjModel)
# admin.site.register(CollarBandBtntModel)
# admin.site.register(CollarBandHeightModel)
# admin.site.register(CuffBtntModel)
# admin.site.register(CuffObjModel)
# admin.site.register(CuffStiffnessModel)
admin.site.register(CuffStyleModel)

# admin.site.register(StyleTypeModel)
# admin.site.register(SleeveTypeModel)
# admin.site.register(ShirtSleeveModel)
# admin.site.register(YokeTypeModel)
# admin.site.register(YokeModel)
# admin.site.register(ShoulderTypeModel)
# admin.site.register(ShoulderModel)
# admin.site.register(BackDetailsTypeModel)
# admin.site.register(BackDetailsModel)
# admin.site.register(BottomCutTypeModel)
# admin.site.register(BottomCutModel)
# admin.site.register(CollarTypeModel)
# admin.site.register(CollarModel)
# admin.site.register(CuffTypeModel)
# admin.site.register(PlacketTypeModel)
# admin.site.register(CuffModel)
# admin.site.register(PlacketModel)
# admin.site.register(CollarButtonModel)
# admin.site.register(CuffButtonModel)
# admin.site.register(PlacketButtonModel)
# admin.site.register(CollarThreadModel)
# admin.site.register(CuffThreadModel)
# admin.site.register(PlacketThreadModel)

class SideBarAdmin(TranslationAdmin):
    pass
admin.site.register(SideBarModel, SideBarAdmin)

class SubSideBarAdmin(TranslationAdmin):
    pass
admin.site.register(SubSideBarModel, SubSideBarAdmin)


# class FooAdmin(admin.ModelAdmin):
#     def render_change_form(self, request, context, *args, **kwargs):
#         context['adminform'].form.fields['extra_foo'].queryset = Foo.objects.filter(extra=True)
#         return super(FooAdmin, self).render_change_form(request, context, *args, **kwargs)
#
# admin.site.register(Foo, FooAdmin)



class StyleSideBarAdmin(TranslationAdmin):
    pass
admin.site.register(StyleSideBarModel, StyleSideBarAdmin)