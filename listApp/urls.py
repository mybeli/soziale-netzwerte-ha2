from django.conf.urls import url
from django.views.generic import TemplateView
from . import views


urlpatterns = [
	url(r'^$', views.todo_list, name='todo_list'),
	url(r'^about', TemplateView.as_view(template_name='listApp/about.html'), name='about'),
	url(r'^listApp/new/$', views.todo_new, name='todo_new'),
	url(r'^listApp/(?P<pk>\d+)/edit/$', views.todo_edit, name = 'todo_edit'),
	url(r'^listApp/(?P<pk>\d+)/delete/$', views.todo_delete, name = 'todo_delete'),
]