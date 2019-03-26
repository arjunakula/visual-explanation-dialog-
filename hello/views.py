from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
from gettingstarted.settings import EXPLANATION_FILES

# Create your views here.
def test(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'test.html')


def test2(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'test2.html')

def test3(request):
    return render(request, 'test3.html')

# for explainer and evaluator demo
def explainer(request):
    return render(request, 'xai_demo_pages/explainer.html')

def attention_maps(request):
    return render(request, 'xai_demo_pages/attention_maps.html')

def x_tom_explanations(request):
    return render(request, 'xai_demo_pages/x_tom_explanations.html')

def wo_explanation(request):
    return render(request, 'xai_demo_pages/wo_explanation.html')

def evaluator(request):
    return render(request, 'xai_demo_pages/evaluator.html')

def evaluator_results(request):
    return render(request, 'xai_demo_pages/evaluator_results.html')


def explanation(request, number):
    filepath = EXPLANATION_FILES + '/explanation' + number + '.txt'
    with open(filepath, 'r') as fp:
        data = fp.read()
    # filename = 'some-filename.xlsx'
    # response = HttpResponse(mimetype="application/ms-excel")
    # response['Content-Disposition'] = 'attachment; filename=%s' % filename # force browser to download file
    response = HttpResponse()
    response.write(data)
    return response

def getImages(request, number):
    filepath = EXPLANATION_FILES + '/demo' + number + '.png'
    with open(filepath, "rb") as f:
        return HttpResponse(f.read(), content_type="image/png")


def getQuestionSet(request):
    filepath = EXPLANATION_FILES + '/questionSet.txt'
    with open(filepath, 'r') as fp:
        data = fp.read()
    # filename = 'some-filename.xlsx'
    # response = HttpResponse(mimetype="application/ms-excel")
    # response['Content-Disposition'] = 'attachment; filename=%s' % filename # force browser to download file
    response = HttpResponse()
    response.write(data)
    return response     


def db(request):
    greeting = Greeting()
    greeting.save()
    greetings = Greeting.objects.all()
    return render(request, 'db.html', {'greetings': greetings})

