from django.contrib import admin
from .models import (
    FabricModel,
    StyleTypeModel,
    SleeveTypeModel,
    ShirtSleeveModel,
    YokeTypeModel,
    YokeModel,
    ShoulderTypeModel,
    ShoulderModel,
    BackDetailsTypeModel,
    BackDetailsModel,
    BottomCutTypeModel,
    BottomCutModel, CollarTypeModel,
    CollarModel, CuffTypeModel, CuffModel, PlacketTypeModel, PlacketModel
)
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
