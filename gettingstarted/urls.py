from django.conf.urls import include, url
from django.urls import path

from django.contrib import admin
admin.autodiscover()

import hello.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', hello.views.test, name='test'),
    url(r'^test.html', hello.views.test, name='test'),
    url(r'^test2.html', hello.views.test2, name='test2'),
    url(r'^test3',hello.views.test3, name='test3'),
    url(r'^explanation(\d+).txt', hello.views.explanation, name = 'explanation'),

    # for explainer and evaluator demo
    url(r'^explainer.html', hello.views.explainer, name = 'explainer'),
    url(r'^attention_maps.html', hello.views.attention_maps, name = 'attention_maps'),
    url(r'^x_tom_explanations.html', hello.views.x_tom_explanations, name = 'x_tom_explanations'),
    url(r'^wo_explanation.html', hello.views.wo_explanation, name = 'wo_explanation'),
    url(r'^evaluator.html', hello.views.evaluator, name = 'evaluator'),
    url(r'^evaluator_results.html', hello.views.evaluator_results, name = 'evaluator_results'),

    url(r'^demo(\d+).png', hello.views.getImages, name = 'getImage'),
    url(r'^questionSet.txt', hello.views.getQuestionSet, name = 'getQuestionSet'),
    url(r'^db', hello.views.db, name='db'),
    path('admin/', admin.site.urls),
]
