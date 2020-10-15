from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(Project)
class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'description_short',)


@register(Partner)
class PostTranslationOptions(TranslationOptions):
    fields = ('name',)
