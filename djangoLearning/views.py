from django.shortcuts import render
# Create your views here.
def dj_Learning(request):
    course_price = {'Django': 600, 'React': 5000, }
    return render(request, 'dj/dj.html', course_price)