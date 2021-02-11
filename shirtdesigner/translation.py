from modeltranslation.translator import register, TranslationOptions
from shirtdesigner.models import (
    SideBarModel,
    SubSideBarModel, StyleSideBarModel
)

@register(SideBarModel)
class SideBarTranslationOptions(TranslationOptions):
    fields = (
        'title',
        )

@register(SubSideBarModel)
class SubSideBarTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(StyleSideBarModel)
class StyleSideBarTranslationOptions(TranslationOptions):
    fields = ('title',)
