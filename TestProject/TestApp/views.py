from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from .serializers import GetQuestionSerializer, GetCorrectAnsSerializer
from .models import Exam, Options, User
# Create your views here.


class GetQuestion(APIView):
    """
    get question and respectable option on the bases of id is passed
    """

    def get(self, request):
        register_data = JSONParser().parse(request)
        _id = register_data["exam_id"]
        question = Exam.objects.filter(exam_id=_id)
        question_serializer = GetQuestionSerializer(question, many=True)
        return JsonResponse({"question": question_serializer.data})

class ValidateAns(APIView):
    """
    get ans and exam id from user and check the ans if true increase the total score

    """
    def post(self, request):
        user_data = JSONParser().parse(request)
        user_ans = user_data["user_ans"]
        exam_id = user_data["exam_id"]
        user_id = user_data["user_id"]
        users = User.objects.get(pk=user_id)
        new_score = users.total_score
        # print(user_score)
        correct_ans = Options.objects.filter(exam_id=exam_id).values("correct_option").first()
        print(correct_ans["correct_option"])
        if user_ans == correct_ans["correct_option"]:
            new_score += 1
        users.total_score = new_score
        users.save()
        return JsonResponse({"user_name": users.name, "total_score": new_score})


