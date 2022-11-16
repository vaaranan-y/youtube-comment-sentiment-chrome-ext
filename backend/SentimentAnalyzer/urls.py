from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get-text-sentiment/', views.get_text_sentiment,
         name='get_text_sentiment'),
]
