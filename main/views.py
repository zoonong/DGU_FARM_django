from django.shortcuts import render
import time

# Create your views here.

def home(request):
    return render(request, 'home.html')

def decode(request):
    originImg = request.POST['hidden'] # 원본 이미지 파일 저장
    time.sleep(6)
    return render(request, 'found.html', {'imgdc':originImg,})