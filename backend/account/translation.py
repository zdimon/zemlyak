from modeltranslation.translator import translator, TranslationOptions
from .models import Country, City, Cafe

class CountryTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(Country, CountryTranslationOptions)

class CityTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(City, CityTranslationOptions)

class CafeTranslationOptions(TranslationOptions):
    fields = ('desc',)

translator.register(Cafe, CafeTranslationOptions)