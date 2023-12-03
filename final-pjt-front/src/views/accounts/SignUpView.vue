<template>
    <div class="box">   
        <h1>회원가입</h1>
        <form @submit.prevent="signUp">
            <div class="input-group mb-3">
                <label for="email" class="input-group-text border-end-0 border-warning">이메일</label>
                <input type="email" class="form-control border border-warning" id="email" v-model="email">
            </div>
            <div class="input-group mb-3">
                <label for="password1" class="input-group-text border-end-0 border-warning">비밀번호</label>
                <input type="password" class="form-control border border-warning" id="password1" v-model="password1">
            </div>
            <div class="input-group mb-3">
                <label for="password2" class="input-group-text border-end-0 border-warning">비밀번호</label>
                <input type="password" class="form-control border border-warning" id="password2" v-model="password2">
            </div>
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
            <button type="submit" class="btn btn-primary">가입!</button>
        </form>        
    </div>  
</template>

<script setup>
import { ref } from 'vue';
import { useUserStore } from '@/stores/user'
const store = useUserStore()

const email = ref(null)
const password1 = ref(null)
const password2 = ref(null)
const username = ref(null)
const birth = ref(null)
const phone = ref(null)
const address = ref(null)
const money = ref(null)
const salary = ref(null)
const married = ref(null)
const main_bank = ref(null)
const save_type = ref(null)
const signUp = function () {
    const userData = {
        "email"     : email.value,
        "password1" : password1.value,
        "password2" : password2.value,
        "username"  : username.value,
        "birth"     : birth.value,
        "phone"     : phone.value,
        "address"   : address.value,
        "products"  : 'NoProd',
        "money"     : money.value,
        "salary"    : salary.value,
        "married"   : married.value,
        "main_bank" : main_bank.value,
        "save_type" : save_type.value,
    }
    store.signUp(userData)
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
.text-box {
    text-align: center;
    margin: 20px;
}
</style>