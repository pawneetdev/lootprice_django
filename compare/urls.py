from django.conf.urls import url, patterns
from compare import views

urlpatterns = [url(r'^$', views.get_name, name = 'index'),
              #url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
              #url(r'^mobile/$', views.mobile, name='mobiles'),
              #url(r'^display/$', views.display, name = 'display'),
              url(r'^search/$', views.search, name = 'search'),
              url(r'^specs/(?P<mobile_id>[0-9]+)$', views.specs, name = 'specs'),
              url(r'^add/', views.compare, name = 'compare'),
              url(r'^add1/(?P<mobile_id>[0-9]+)$', views.add, name = 'add'),
              url(r'^remove/(?P<mobile_id>[0-9]+)$', views.remove, name = 'remove')
              ]
