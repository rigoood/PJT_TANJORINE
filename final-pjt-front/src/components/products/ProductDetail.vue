<template>
    <div>
        <h3><span class="badge bg-warning">상품 상세 정보</span></h3>
        <div class="input-group">
            <p class="input-group-text border-end-0 border-warning title">은행명</p>
            <p class="form-control border border-warning" >{{ dataProd.kor_co_nm }}</p>
        </div>
        <div class="input-group">
            <p class="input-group-text border-end-0 border-warning title">상품명</p>
            <p class="form-control border border-warning" >{{ dataProd.fin_prdt_nm}}</p>
        </div>
        <div class="input-group">
            <p class="input-group-text border-end-0 border-warning title">공시제출월</p>
            <p class="form-control border border-warning" >{{ dataProd.dcls_month}}</p>
        </div>
        <div class="input-group">
            <p class="input-group-text border-end-0 border-warning title">가입대상</p>
            <p class="form-control border border-warning" >{{ dataProd.join_member}}</p>
        </div>
        <div class="input-group">
            <p class="input-group-text border-end-0 border-warning title">가입방법</p>
            <p class="form-control border border-warning" >{{ dataProd.join_way}}</p>
        </div>
        <div class="input-group">
            <p class="input-group-text border-end-0 border-warning title">우대조건</p>
            <p class="form-control border border-warning" >{{ dataProd.spcl_cnd}}</p>
        </div>
        <div class="input-group">
            <p class="input-group-text border-end-0 border-warning title">만기후 이자율</p>
            <p class="form-control border border-warning" >{{ dataProd.mtrt_int}}</p>
        </div>
        <div class="input-group">
            <p class="input-group-text border-end-0 border-warning title">기타</p>
            <p class="form-control border border-warning" >{{ dataProd.etc_not}}</p>
        </div>
    </div>
</template>

<script setup>
import { onMounted, ref } from 'vue';
const prodData = defineProps({
    dataProd: Object
    })
    
</script>

<style scoped>
.title {
    width: 130px;
}
</style>