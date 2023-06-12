from django.contrib import admin
from about.models import AboutModel, AboutInformation, LearningModel, HireMeModel, ExprementModel, EducationModel, ExperienceModel

# Register your models here.

admin.site.register(AboutModel)
admin.site.register(AboutInformation)
admin.site.register(LearningModel)
admin.site.register(HireMeModel)
admin.site.register(ExprementModel)
admin.site.register(EducationModel)
admin.site.register(ExperienceModel)