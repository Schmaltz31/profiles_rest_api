from django.conf.urls import url

from . import views


urlpattern = [
    url(r'^hello-view/', views.HelloApiView.as_view()),
]
