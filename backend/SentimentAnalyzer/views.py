from django.shortcuts import render
# from .apps import WebappConfig
from django.http import HttpResponse, JsonResponse
# Create your views here.
import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import os
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
nltk.downloader.download('vader_lexicon')


def index(request):
    return HttpResponse("Welcome to the sentiment analyzer of this app!")


def get_text_sentiment(request):

    # PERFORM SENTIMENT ANALYSIS HERE

    sentimentResult = 0

    sampleText = "I am excited and thrilled to use this sentiment analyzer!!!"

    sia = SentimentIntensityAnalyzer()  # the actual analyzer
    sentimentResult = sia.polarity_scores(sampleText)
    return HttpResponse("Result of text sentiment here: " + str(sentimentResult['compound']))
