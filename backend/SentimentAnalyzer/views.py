from django.shortcuts import render
from .apps import WebappConfig
from django.http import HttpResponse, JsonResponse
# Create your views here.


def index(request):
    return HttpResponse("Welcome to the sentiment analyzer of this app")


def get_text_sentiment(self, request):
    # print(request)
    # print('text given: ', text)
    # print('request body: ', request.body)

    # PERFORM SENTIMENT ANALYSIS HERE
    params = request.GET.get('comment')

    response = WebappConfig.predictor.predict(params)

    return JsonResponse(response)
