"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from boards import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^boards/(?P<pk>\d+)/$', views.board_topics, name='board_topics'),
    url(r'^boards/(?P<pk>\d+)/new/$', views.new_topic, name='new_topic'),

    # simple URL routing
    # Simple URL structure
    # url(r'^about/$', views.about, name='about'),

    # deeper URL structures:
    # url(r'^about/company/$', views.about_company, name='about_company'),
    # url(r'^about/author/$', views.about_author, name='about_author'),
    # url(r'^about/author/raihan/$', views.about_raihan, name='about_raihan'),
    # url(r'^privacy/$', views.privacy_policy, name='privacy_policy'),

    # Advanced URLs
    # url(r'^(?P<username>[\w.@+-]+)/$', views.user_profile, name='user_profile'),
    url(r'^admin/', admin.site.urls),
]
