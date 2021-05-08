from django.conf.urls import url
from .import views
from django.urls import path
# app_name = "patient_app"

urlpatterns = [

    url(r'^question/$', views.GetQuestion.as_view()),
    url(r'^validate/$', views.ValidateAns.as_view())

]
