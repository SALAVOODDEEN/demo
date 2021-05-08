from django.shortcuts import render
from .models import Departments, Doctors, Appointment
from django.views.generic import (TemplateView, ListView,
                                  DetailView, CreateView,
                                  UpdateView, DeleteView)
from django.http import JsonResponse
from rest_framework.views import APIView
from .serializers import DepartmentSerializer
from django.shortcuts import HttpResponse, render, redirect
from django.core.exceptions import ValidationError
from django.urls import reverse_lazy
from .forms import ContactForm
# Create your views here.


def home(request):
    return render(request, "patient_app/index.html")

def about(request):
    return render(request, "patient_app/about.html")


class DepartmentView(ListView):

    def get(self, request, **kwargs):
        context = Departments.objects.all()
        # department_data = DepartmentSerializer(context, many=True)
        department_dict = {"departments": context}
        return render(request, "patient_app/department_list.html", department_dict)


class DoctorsView(ListView):

    def get(self, request, **kwargs):
        context = Doctors.objects.all()
        doctors_dict = {"doctors": context}
        return render(request, "patient_app/doctors_list.html", doctors_dict)


class AppointmentRegisterView(CreateView):
        model = Appointment
        fields = "__all__"
        from_class = ContactForm
        success_url = reverse_lazy('home')
        template_name = "patient_app/appointment.html"

    # def post(self, request, **kwargs):
    #     model = Appointment
    #     form = ContactForm(request.POST)
    #     if form.is_valid():
    #         form.save(commit=True)
    #         return home(request)
    #     else:
    #         print("form invalid !!")
    #     return render(request, "patient_app/appointment.html", {"form": form})



# class DoctorsRegister(CreateView):
#
#     def post(self, request, **kwargs):
#
#         form = ContactForm
#         if form.is_valid():
#             data = form.save(commit=False)
#             data.save()
#             return HttpResponse("data submitted successfully")
#
#         if not form.is_valid():
#             raise ValidationError(" invalid form !!")
#
#         return render(request, 'patient_app/index.html', {'form': form})
