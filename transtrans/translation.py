from modeltranslation.translator import translator, TranslationOptions
from sections.models import Section

class SectionTranslationOptions(TranslationOptions):
        fields = ('title', 'description',)

translator.register(Section, SectionTranslationOptions)
