from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.conf import settings
from django.http import JsonResponse
from datetime import datetime
import requests

# Create your views here.
@api_view(['GET'])
def index(request):
    # 날짜: YYYYMMDD
    today = ''.join(str(datetime.today())[:10].split('-'))

    # 요일: 0:월 ~ 6:일  -> 토, 일 : 금요일 환율 보여주기
    day = datetime.today().weekday()
    if day == 5:
        today = str(int(today) - 1)
    elif day == 6:
        today = str(int(today) - 2)

    APIKEY = settings.EXCHANGE_RATE_API_KEY
    DATE=today # YYYYMMDD
    TYPE='AP01'  # AP01: 환율 / AP02: 대출금리 / AP03: 국제금리
    url = f'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={APIKEY}&searchdate={DATE}&data={TYPE}'

    response = requests.get(url).json()
    return Response(response)
    # return Response({'date':DATE}, data=response)