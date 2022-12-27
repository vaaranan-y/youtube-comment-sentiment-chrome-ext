from django.shortcuts import render
from django.template import loader
# from .apps import WebappConfig
from django.http import HttpResponse, JsonResponse
# Create your views here.
import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import os
import nltk
import requests
import json
import config
from nltk.sentiment import SentimentIntensityAnalyzer
nltk.downloader.download('vader_lexicon')


def index(request):
    return HttpResponse("Welcome to the sentiment analyzer of this app!")


def get_text_sentiment_helper(text):

    # PERFORM SENTIMENT ANALYSIS HERE

    sia = SentimentIntensityAnalyzer()  # the actual analyzer
    sentimentResult = sia.polarity_scores(text)
    return sentimentResult['compound']


def get_video_sentiment(request, videoId):

    # GET RESULTS FOR SENTIMENT ANALYSIS OF VIDEO
    url = config.api_url + videoId
    headers = {'X-RapidAPI-Key': config.api_key,
               'X-RapidAPI-Host': config.api_host}
    params = {'videoId': videoId}
    res = requests.get(url, params=params, headers=headers)
    print(res.content)

    data = res.json()['items']
    scoreSum = 0
    scoreCount = 0
    for comment in data:
        currSentimentScore = get_text_sentiment_helper(comment['contentText'])
        # print("Comment: ", comment['contentText'], "\n")
        # print("SentimentScore: ", str(currSentimentScore), "\n")
        scoreSum += currSentimentScore
        scoreCount += 1

    averageSentiment = scoreSum/scoreCount
    print("Average Sentiment: ", str(averageSentiment))

    response = {"avgSentiment": averageSentiment}

    return JsonResponse(json.loads(json.dumps(response)))


def get_text_sentiment(request, text):

    # PERFORM SENTIMENT ANALYSIS HERE

    # sampleText = "I am excited and thrilled to use this sentiment analyzer!!!"

    sampleText = text.replace("-", " ")

    sia = SentimentIntensityAnalyzer()  # the actual analyzer
    sentimentResult = sia.polarity_scores(sampleText)

    template = loader.get_template('myfirst.html')

    # gives overall result
    data = {
        'result': str(sentimentResult['compound'])
    }
    return JsonResponse(data)

    # return HttpResponse(template.render())
