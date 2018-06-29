from django.conf.urls import include, url
from base.views import Home, TaskView, AssignmentView
from django.contrib.auth import views
from base.forms import LoginForm

urlpatterns = [
    url(r'^$', Home.as_view(), name='home'),
    url(r'^login/', views.login, {'template_name': 'login.html', 'authentication_form': LoginForm}),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
                          {'next_page': '/'}),
    url(r'^task/$', TaskView.as_view(), name='task'),
	url(r'^assign/$', AssignmentView.as_view(), name='assign'),
]
