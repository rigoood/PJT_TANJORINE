# from django.shortcuts import render
from rest_framework.response import Response
# from django.http import JsonResponse
from django.conf import settings
from rest_framework.decorators import api_view
import requests

# # Create your views here.
@api_view(['GET'])
def bank(request):
    APIKEY = settings.FIN_API_KEY
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={APIKEY}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()
    return Response(response)