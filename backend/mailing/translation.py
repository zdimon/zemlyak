from modeltranslation.translator import translator, TranslationOptions
from mailing.models import EmailTemplate

class EmailTemplateTranslationOptions(TranslationOptions):
    fields = ('title', 'content')

translator.register(EmailTemplate,EmailTemplateTranslationOptions)

