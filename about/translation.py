from modeltranslation.translator import TranslationOptions, register
from about.models import AboutModel, AboutInformation, LearningModel, HireMeModel, ExprementModel, EducationModel, ExperienceModel

@register(AboutModel)
class AboutModelTranslationOptions(TranslationOptions):
    fields = ('title', 'name', 'work_name', 'body')



@register(AboutInformation)
class AboutInformationTranslationOptions(TranslationOptions):
    fields = ('title', 'information')


@register(LearningModel)
class LearningModelTranslationOptions(TranslationOptions):
    fields = ('name', )


@register(HireMeModel)
class HireMeModelTranslationOptions(TranslationOptions):
    fields = ('title',)



@register(ExprementModel)
class ExprementModelTranslationOptions(TranslationOptions):
    fields = ('education', 'experience')



@register(EducationModel)
class EducationModelTranslationOptions(TranslationOptions):
    fields = ('title', 'body')


@register(ExperienceModel)
class ExprementModelTranslationOptions(TranslationOptions):
    fields = ('title', 'body')