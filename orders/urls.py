from django.conf.urls import patterns, url

urlpatterns = patterns('orders.views',
    url(r'^orders-history/$', 'orders_history'),
    url(r'^who-work-today/$', 'who_work_today'),
    url(r'^order/$', 'order'),
    url(r'^argent/$', 'argent'),
    url(r'^$', 'home'),
)
