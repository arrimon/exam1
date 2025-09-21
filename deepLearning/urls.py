from django.contrib import admin
from django.urls import path
from deepLearning.views import d_Learning
urlpatterns = [
    path('dl/', d_Learning),
]