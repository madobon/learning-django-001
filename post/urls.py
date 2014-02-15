from django.conf.urls import patterns, url

from post import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    # url(r'^send/$', views.send, name='send'),
    # url(r'^result/$', views.result, name='result'),
)