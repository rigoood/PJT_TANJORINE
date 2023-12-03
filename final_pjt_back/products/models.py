from django.db import models
# Create your models here.
class DepositProduct(models.Model):
    dcls_month      = models.CharField(max_length=30)             # 공시제출월
    fin_co_no       = models.CharField(max_length=30)             # 금융회사코드
    kor_co_nm       = models.CharField(max_length=30)             # 금융회사명
    fin_prdt_cd     = models.CharField(max_length=30)             # 금융상품코드
    fin_prdt_nm     = models.CharField(max_length=30)             # 금융상품명
    join_way        = models.CharField(max_length=30, null=True)  # 가입방법
    mtrt_int        = models.CharField(max_length=100, null=True) # 만기 후 이자율
    spcl_cnd        = models.CharField(max_length=100, null=True) # 우대조건
    join_deny       = models.CharField(max_length=30, null=True)  # 가입제한
    join_member     = models.CharField(max_length=30, null=True)  # 가입대상
    etc_note        = models.CharField(max_length=100, null=True) # 기타유의사항
    max_limit       = models.IntegerField(null=True)              # 최고한도
    dcls_strt_day   = models.CharField(max_length=30, null=True)  # 공시시작일
    dcls_end_day    = models.CharField(max_length=30, null=True)  # 공시종료일
    fin_co_subm_day = models.CharField(max_length=30, null=True)  # 금융회사 제출일


class DepositOption(models.Model):
    dcls_month =        models.CharField(max_length=30)            # 공시제출월
    product =           models.ForeignKey(DepositProduct, on_delete=models.CASCADE, related_name='option')
    intr_rate_type =    models.CharField(max_length=30, null=True) # 저축금리유형
    intr_rate_type_nm = models.CharField(max_length=30, null=True) # 저축금리유형명
    save_trm =          models.CharField(max_length=30, null=True) # 저축기간
    intr_rate =         models.FloatField(null=True)               # 저축금리
    intr_rate2 =        models.FloatField(null=True)               # 최고우대금리

class SavingProduct(models.Model):
    dcls_month      = models.CharField(max_length=30)             # 공시제출월
    fin_co_no       = models.CharField(max_length=30)             # 금융회사코드
    kor_co_nm       = models.CharField(max_length=30)             # 금융회사명
    fin_prdt_cd     = models.CharField(max_length=30)             # 금융상품코드
    fin_prdt_nm     = models.CharField(max_length=30)             # 금융상품명
    join_way        = models.CharField(max_length=30, null=True)  # 가입방법
    mtrt_int        = models.CharField(max_length=100, null=True) # 만기 후 이자율
    spcl_cnd        = models.CharField(max_length=100, null=True) # 우대조건
    join_deny       = models.CharField(max_length=30, null=True)  # 가입제한
    join_member     = models.CharField(max_length=30, null=True)  # 가입대상
    etc_note        = models.CharField(max_length=100, null=True) # 기타유의사항
    max_limit       = models.IntegerField(null=True)              # 최고한도
    dcls_strt_day   = models.CharField(max_length=30, null=True)  # 공시시작일
    dcls_end_day    = models.CharField(max_length=30, null=True)  # 공시종료일
    fin_co_subm_day = models.CharField(max_length=30, null=True)  # 금융회사 제출일

class SavingOption(models.Model):
    dcls_month =        models.CharField(max_length=30)            # 공시제출월
    product =           models.ForeignKey(SavingProduct, on_delete=models.CASCADE, related_name='option')
    intr_rate_type =    models.CharField(max_length=30, null=True) # 저축금리유형
    intr_rate_type_nm = models.CharField(max_length=30, null=True) # 저축금리유형명
    rsrv_type =         models.CharField(max_length=30, null=True) # 적립유형
    rsrv_type_nm =      models.CharField(max_length=30, null=True) # 적립유형명
    save_trm =          models.CharField(max_length=30, null=True) # 저축기간
    intr_rate =         models.FloatField(null=True)               # 저축금리
    intr_rate2 =        models.FloatField(null=True)               # 최고우대금리

class IntegratedProduct(models.Model):
    code = models.CharField(max_length=30) # 타입 /$ 회사코드 /$ 상품코드