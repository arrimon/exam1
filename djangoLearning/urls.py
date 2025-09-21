from django.contrib import admin
from django.urls import path
from djangoLearning.views import dj_Learning
urlpatterns = [
    path('dj/', dj_Learning),

]