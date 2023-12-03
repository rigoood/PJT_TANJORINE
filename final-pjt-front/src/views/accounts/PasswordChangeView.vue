<template>
    <div class="box">
        <div class="text-box">
            <h1>비밀번호 변경</h1>
        </div>        
        <form @submit.prevent="password_change">
            <div class="input-group mb-3 border border-warning">
                <span class="input-group-text">비밀번호</span>
                <input type="password" class="form-control" placeholder="password" v-model="pw1">
            </div>            
            <div class="input-group mb-3 border border-warning">
                <span class="input-group-text">비밀번호 재확인</span>
                <input type="password" class="form-control" placeholder="Password" v-model="pw2">
            </div>
            <button class="btn btn-warning" type="submit">변경</button>            
        </form>
    </div>
</template>

<script setup>
import axios from 'axios';
import { ref } from 'vue';
import { useUserStore } from '@/stores/user'
import { useRouter } from 'vue-router';
const router = useRouter()
const userstore = useUserStore()
const pw1 = ref(null)
const pw2 = ref(null)
const password_change = function() {
    axios({
      method: 'post',
      url: `http://127.0.0.1:8000/accounts/password/change/`,
      headers: {
          Authorization: `Token ${userstore.token}`
      },
      data: {
        new_password1: pw1.value,
        new_password2: pw2.value,
      }
    })
    .then((res) => {
        console.log(res)
        alert(res.data.detail)
        router.push({name: 'home'})
    })
}
</script>

<style scoped>
span {
    width: 130px;
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