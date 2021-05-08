from rest_framework import serializers
from .models import Departments, Doctors


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = '__all__'
