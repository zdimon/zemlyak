from modeltranslation.translator import translator, TranslationOptions
from .models import Name, Prof

class NameTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(Name, NameTranslationOptions)

class ProfTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(Prof, ProfTranslationOptions)