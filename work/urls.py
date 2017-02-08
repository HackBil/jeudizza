from django.conf.urls import patterns, url

urlpatterns = patterns('work.views',
    url(r'^random-chores/$', 'random_chores'),
)
