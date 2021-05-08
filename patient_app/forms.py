from django import forms
from django.core.exceptions import ValidationError
from .models import Departments, Doctors, Appointment
from django.core import validators
import re
class ContactForm(forms.ModelForm):
    # phone_no = forms.IntegerField()

    def clean(self):
        all_cleaned_data = super().clean()
        phone_no = all_cleaned_data["phone_no"]
        pattern = r"^[0-9]{10}$"
        rule1 = re.compile(pattern)
        if not rule1.search(phone_no):
            raise forms.ValidationError("invalid mobile !!")

    class Meta:
        model = Appointment
        fields = "__all__"


