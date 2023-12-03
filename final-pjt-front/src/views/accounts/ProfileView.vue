<template>
    <div class="container">
        <div class="row">
            <div class="col-3 m-1 mt-3 p-3 border border-warning border-3 d-flex flex-column ivory">
                <h1><span class="badge bg-primary">회원 정보</span></h1>
                <p>실 명 : {{ username }}</p>
                <p>생년월일 : {{ birth }}</p>
                <p>휴대폰 : {{ phone }}</p>
                <p>주 소 :{{ address }}</p>
                <p>자산 : {{ money }}</p>
                <p>연봉 : {{ salary }}</p>
                <p>결혼 :{{ married ? '기혼' : '미혼' }}</p>
                <p>주거래은행 : {{ main_bank }}</p>
                <p>저축 성향 : {{ save_nm }}</p>

                <div class="d-flex flex-column mt-auto">
                    <RouterLink class="btn btn-warning m-1" :to="{ name: 'profileUpdate', props:data}">수정</RouterLink>
                    <RouterLink class="btn btn-warning m-1" :to="{ name: 'passwordChange'}">비밀번호 변경</RouterLink>
                </div>
            </div>
            <div class="col-8 m-1 mt-3 border border-warning border-3 d-flex flex-column ivory">
                <div class="m-3">
                    <h4><span class="badge bg-primary">가입 상품 목록</span></h4>
                    <template v-for="prod in prodstore.userProd">
                        <div>
                            {{ prod[0].kor_co_nm }} - {{ prod[0].fin_prdt_nm }}
                        </div>
                    </template>
                </div>
                <div class="m-3">
                    <h4><span class="badge bg-primary">가입 상품 금리 비교</span></h4>
                    <div>
                        <chart/>
                    </div>
                </div>
                <div class="m-3">
                    <h4><span class="badge bg-warning">추천 상품</span></h4>
                    <template v-for="data in Object.keys(algoData)" :key="data">
                        <p>{{ data + ' 번째 ' + algoData[data][0].kor_co_nm }} - <RouterLink :to="{name:'productDetail', params:{type:algoData[data][1], id: algoData[data][0].id}}">{{ algoData[data][0].fin_prdt_nm }}</RouterLink></p>
                        
                    </template>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'
import { ref, onMounted, onBeforeMount, computed } from 'vue';
import { useUserStore } from '@/stores/user'
import { useProductStore } from '@/stores/product'
import chart from '@/components/products/chart.vue'
import axios from 'axios';


const userstore = useUserStore()
const prodstore = useProductStore()

const data = ref(null)
const username = ref(null)
const birth = ref(null)
const phone = ref(null)
const address = ref(null)
const money = ref(null)
const salary = ref(null)
const married = ref(null)
const main_bank = ref(null)
const save_type = ref(null)
const algoData = ref([])
const save_nm = computed(() => {
    if (save_type.value === 1) return '예금우선'
    else if (save_type.value === 2) return '적금우선'
    else if (save_type.value === 3) return '소비우선'
    else if (save_type.value === 4) return '복합'
})

const pageDataLoad = function() {
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/accounts/user/`,
      headers: {
          Authorization: `Token ${userstore.token}`
      }
    }).then((res) => {
        // 프로필 수정 화면 표시용
        data.value = res.data

        username.value  = res.data.username
        birth.value     = res.data.birth
        phone.value     = res.data.phone
        address.value   = res.data.address
        money.value     = res.data.money
        salary.value    = res.data.salary
        married.value   = res.data.married
        main_bank.value = res.data.main_bank
        save_type.value = res.data.save_type
        prodstore.signedProductsInfo(res.data.products.split(',').map(d=> d.split('/$')))
        // 추천상품 받기
        pageAlgoLoad()
    })
}

const pageAlgoLoad = function() {
    const data = {
        email: userstore.userEmail,
        birth: birth.value.slice(0,4),
        married: married.value,
        save_type: save_type.value,
        salary: salary.value,
        money: money.value
    }
    axios({
      method: 'POST',
      url: `http://127.0.0.1:8000/products/algo/`,
      data: data
    })
    .then((res) => {
        console.log(res.data.prods)
        algoData.value = res.data.prods
    })
}

onBeforeMount(() => {
    pageDataLoad()
    
})


</script>

<style scoped>
    form {
        display: flex;
        flex-direction: column;
        width: 350px;
    }
    .line {
        display: flex;
    }
    .btn-box {
        text-decoration: none;
        color: black;
    }
    .ivory {
        color: #ffffff;
    }
</style>