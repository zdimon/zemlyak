from modeltranslation.translator import translator, TranslationOptions
from .models import Country, City, Cafe, UserProfile

class UserProfileTranslationOptions(TranslationOptions):
    fields = ('publicname', 'prof')

translator.register(UserProfile, UserProfileTranslationOptions)

class CountryTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(Country, CountryTranslationOptions)

class CityTranslationOptions(TranslationOptions):
    fields = ('name', 'region')

translator.register(City, CityTranslationOptions)

class CafeTranslationOptions(TranslationOptions):
    fields = ('desc','address')

translator.register(Cafe, CafeTranslationOptions)