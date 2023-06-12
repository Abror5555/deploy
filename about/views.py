from django.shortcuts import render
from about.models import AboutModel, AboutInformation, LearningModel, HireMeModel, ExprementModel, EducationModel, ExperienceModel

# Create your views here.

def about(reuqets):
    about = AboutModel.objects.all()
    information = AboutInformation.objects.all()
    learning = LearningModel.objects.all()
    hire = HireMeModel.objects.all()
    exprement = ExprementModel.objects.all()
    education = EducationModel.objects.all()
    experience = ExperienceModel.objects.all()

    context = {
        'about': about,
        'information': information,
        'learning': learning,
        'hire': hire,
        'exprement': exprement,
        'education': education,
        'experience': experience
    }
    return render(reuqets, 'ab/about.html', context)