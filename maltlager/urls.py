from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login_view, name='login_view'),
    url(r'^logout/$', views.logout_view, name='logout_view'),
    url(r'^hops/$', views.hops, name='hops'),
    url(r'^malt_form/$', views.malt_form, name='malt_form'),
    url(r'^hops_form/$', views.hops_form, name='hops_form'),
    url(r'^history/malt/$', views.history_malt, name='history_malt'),
    url(r'^history/hops/$', views.history_hops, name='history_hops'),
    url(r'^malt_history/(?P<current_malt>.+)/$', views.malt_history, name='malt_history'),
    url(r'^hops_history/(?P<current_hops>.+)/$', views.hops_history, name='hops_history'),
    url(r'^malt/(?P<current_malt>.+)/$', views.update_malt_form, name='update_malt_form'),
    url(r'^hops/(?P<current_hops>.+)/$', views.update_hops_form, name='update_hops_form'),
]
