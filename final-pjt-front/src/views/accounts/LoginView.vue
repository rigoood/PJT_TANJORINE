<template>
    <div class="box">
        <div class="text-box">
            <h1>로그인</h1>
        </div>
        <form @submit.prevent="logIn">
            <div class="input-group mb-3 border border-warning">
                <span class="input-group-text" id="basic-addon1">Email</span>
                <input type="text" class="form-control" placeholder="Email" v-model="email">
            </div>
            <div class="input-group mb-3 border border-warning">
                <span class="input-group-text">PassWord</span>
                <input type="password" class="form-control" placeholder="Password" v-model="password">
            </div>
            <button class="btn btn-warning" type="submit">Log In!</button>
        </form>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import { useUserStore } from '@/stores/user'
const email = ref(null)
const password = ref(null)
const store = useUserStore()
const logIn = function() {
    const loginData = {
        email: email.value,
        password: password.value
    }
    store.logIn(loginData)
}
</script>

<style scoped>
span {
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