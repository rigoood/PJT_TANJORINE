from .models import *
from rest_framework import serializers

class DepositProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProduct
        fields = '__all__'

class SavingProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingProduct
        fields = '__all__'


class DepositOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositOption
        fields = '__all__'
        
class SavingOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingOption
        fields = '__all__'



# 은행 목록 용 시리얼 라이져
class DepositBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProduct
        fields = ('fin_co_no', 'kor_co_nm',)

class SavingBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingProduct
        fields = ('fin_co_no', 'kor_co_nm',)
