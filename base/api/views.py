from django.http import JsonResponse

from base.models import Question
from .serializers import QuestionSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def votingData(request):
    questions = Question.objects.all()
    backend = Question.objects.filter(answer='backend').count()
    frontend = Question.objects.filter(answer='frontend').count()
    fullstack = Question.objects.filter(answer='fullstack').count()
    # serializer = QuestionSerializer(questions, many=True)
    return Response({'backend': backend, 'frontend': frontend, 'fullstack': fullstack})