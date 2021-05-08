from rest_framework import serializers
from .models import Exam, Options, User


class GetOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Options
        fields = ("option_1", "option_2", "option_3", "option_4")


class GetQuestionSerializer(serializers.ModelSerializer):
    options = GetOptionsSerializer(source='options_set', many=True, read_only=True)

    class Meta:
        model = Exam
        fields = '__all__'

class GetCorrectAnsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Options
        fields = ("correct_option", )

