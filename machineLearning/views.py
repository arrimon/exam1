from django.shortcuts import render

# Create your views here.
def m_Learning(request):
    return render(request, 'ml/ml.html')