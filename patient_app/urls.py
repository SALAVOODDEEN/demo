from django.conf.urls import url
from .import views
from django.urls import path
# app_name = "patient_app"

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^about/$', views.about, name="about"),
    url(r'^departments/$', views.DepartmentView.as_view(), name="departments"),
    url(r'^doctors/$', views.DoctorsView.as_view(), name="doctors"),
    url(r'^appointment/$', views.AppointmentRegisterView.as_view(), name="appointment"),
]
