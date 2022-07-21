from modeltranslation.translator import translator, TranslationOptions
from .models import Country, City

class CountryTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(Country, CountryTranslationOptions)

class CityTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(City, CityTranslationOptions)