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
from nltk.sentiment import SentimentIntensityAnalyzer
nltk.downloader.download('vader_lexicon')


def index(request):
    return HttpResponse("Welcome to the sentiment analyzer of this app!")


def get_text_sentiment_helper(text):

    # PERFORM SENTIMENT ANALYSIS HERE

    sia = SentimentIntensityAnalyzer()  # the actual analyzer
    sentimentResult = sia.polarity_scores(text)
    return str(sentimentResult['compound'])


def get_video_sentiment(request, videoId):

    # GET RESULTS FOR SENTIMENT ANALYSIS OF VIDEO
    url = 'https://youtube-media-downloader.p.rapidapi.com/v2/video/comments?videoId=' + videoId
    headers = {'X-RapidAPI-Key': 'edd8f2fcebmsh894c403ec9b1200p16168djsnf80ebdb7e7c0',
               'X-RapidAPI-Host': 'youtube-media-downloader.p.rapidapi.com'}
    params = {'videoId': videoId}
    res = requests.get(url, params=params, headers=headers)
    # print(res.content)

    data = res.json()['items']
    for comment in data:
        print("Comment: ", comment['contentText'], "\n")
        print("SentimentScore: ", get_text_sentiment_helper(
            comment['contentText']), "\n")
    print(type(data))

    return JsonResponse(res.json())


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
