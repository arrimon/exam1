from django.contrib import admin
from django.urls import path
from machineLearning.views import m_Learning

urlpatterns = [
    path('', m_Learning),

]