<template>
    <div class="box">   
        <h1>회원 정보 수정</h1>
        <form @submit.prevent="Update">
            <div class="input-group mb-3">
                <label for="username" class="input-group-text border-end-0 border-warning">이름</label>
                <input type="text" class="form-control border border-warning" id="username" v-model="username">
            </div>
            <div class="input-group mb-3">
                <label for="birth" class="input-group-text border-end-0 border-warning">생일</label>
                <input type="date" class="form-control border border-warning" id="birth" v-model="birth">
            </div>
            <div class="input-group mb-3">
                <label for="phone" class="input-group-text border-end-0 border-warning">휴대폰</label>
                <input type="text" class="form-control border border-warning" id="phone" v-model="phone">
            </div>
            <div class="input-group mb-3">
                <label for="address" class="input-group-text border-end-0 border-warning">주소</label>
                <input type="text" class="form-control border border-warning" id="address" v-model="address">
            </div>
            <div class="input-group mb-3">
                <label for="money" class="input-group-text border-end-0 border-warning">자산</label>
                <input type="number" class="form-control border border-warning" id="money" v-model="money">
            </div>
            <div class="input-group mb-3">
                <label for="salary" class="input-group-text border-end-0 border-warning">연봉</label>
                <input type="number" class="form-control border border-warning" id="salary" v-model="salary">
            </div>
            <div class="input-group mb-3">
                <label for="main_bank" class="input-group-text border-end-0 border-warning">주거래은행</label>
                <input type="text" class="form-control border border-warning" id="main_bank" v-model="main_bank">
            </div>
            <div class="input-group mb-3">
                <label for="" class="input-group-text border-end-0 border-warning">결혼 여부</label>
                <div class="form-control border border-warning">
                    <div class="form-check form-check-inline">
                        <input class="form-check-input" type="radio" name="inlineRadioOptions" id="married1" value="false" v-model="married">
                        <label class="form-check-label" for="married1">미혼</label>
                    </div>
                    <div class="form-check form-check-inline">
                        <input class="form-check-input" type="radio" name="inlineRadioOptions" id="married2" value="true" v-model="married">
                        <label class="form-check-label" for="married2">기혼</label>
                    </div>
                </div>
            </div>
            <div class="input-group mb-3">
                <label for="" class="input-group-text border-end-0 border-warning">저축 성향</label>
                <div class="form-control border border-warning">
                    <div class="form-check form-check-inline">
                        <input class="form-check-input" type="radio" name="type" id="save_type1" value="1" v-model="save_type">
                        <label class="form-check-label" for="save_type1">예금우선</label>
                    </div>
                    <div class="form-check form-check-inline">
                        <input class="form-check-input" type="radio" name="type" id="save_type2" value="2" v-model="save_type">
                        <label class="form-check-label" for="save_type2">적금우선</label>
                    </div>
                    <div class="form-check form-check-inline">
                        <input class="form-check-input" type="radio" name="type" id="save_type3" value="3" v-model="save_type">
                        <label class="form-check-label" for="save_type3">소비우선</label>
                    </div>
                    <div class="form-check form-check-inline">
                        <input class="form-check-input" type="radio" name="type" id="save_type4" value="4" v-model="save_type">
                        <label class="form-check-label" for="save_type4">복합</label>
                    </div>
                </div>
            </div>
            <button type="submit" class="btn btn-primary">변경!</button>
        </form>
    </div>  
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useUserStore } from '@/stores/user'
import { useRouter } from 'vue-router';
import axios from 'axios';

const store = useUserStore()
const router = useRouter()
const username = ref('')
const birth = ref('')
const phone = ref('')
const address = ref('')
const money = ref('')
const salary = ref('')
const married = ref('')
const main_bank = ref('')
const save_type = ref('')
onMounted(() => {
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/accounts/user/`,
      headers: {
          Authorization: `Token ${store.token}`
      }
    }).then((res) => {
        // 프로필 화면 표시용
        username.value  = res.data.username
        birth.value     = res.data.birth
        phone.value     = res.data.phone
        address.value   = res.data.address
        money.value     = res.data.money
        salary.value    = res.data.salary
        married.value   = res.data.married
        main_bank.value = res.data.main_bank
        save_type.value = res.data.save_type
    })
})

const Update = function() {
    const userData = {
        "username"  : username.value,
        "birth"     : birth.value,
        "phone"     : phone.value,
        "address"   : address.value,
        "money"     : money.value,
        "salary"    : salary.value,
        "married"   : married.value,
        "main_bank" : main_bank.value,
        "save_type" : save_type.value,
    }
    axios({
      method: 'put',
      url: `http://127.0.0.1:8000/accounts/user/`,
      headers: {
          Authorization: `Token ${store.token}`
      },
      data: userData
    }).then((res) => {
        // 프로필 화면 표시용
        router.push({ name: 'profile' })
    })
}
</script>

<style scoped>
label {
    width: 100px;
}
.box {
    width: 40%;
    min-width: 500px;
    margin: 30px;
}
</style>