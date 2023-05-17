from django.shortcuts import render
from .models import File, Category, Product
from .disain import Disain
from .report import Report
from .study import Study



def project(request):
    files = File.objects.all()
    category = Category.objects.all()
    projects = Product.objects.all()
    context = {
        "category": category,
        "projects": projects,
        "files": files,
    }
    return render(request, 'project/project.html', context )



def disain(request):
    disain = Disain.objects.all()
    context = {
        "disain": disain,
    }
    return render(request, 'project/disain.html', context )


def report(request):
    report = Report.objects.all()
    context = {
        "report": report,
    }
    return render(request, 'project/report.html', context )


def study(request):
    study = Study.objects.all()
    context = {
        "study": study,
    }
    return render(request, 'project/study.html', context )