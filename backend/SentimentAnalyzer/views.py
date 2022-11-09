from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("Welcome to the sentiment analyzer of this app")


def get_text_sentiment(request, text):

    print('text given: ', text)

    # PERFORM SENTIMENT ANALYSIS HERE

    return HttpResponse("Sentiment Analysis Result: %s", "UNKNOWN")
