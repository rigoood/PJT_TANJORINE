<template>
  <header>
    <nav class="navbar navbar-expand-md brown">
      <div class="container-fluid d-flex align-items-center">
        <div class="mx-5">
          <a class="navbar-brand" href="#">
            <img src="./assets/tangerine2.png" width="40" alt="">
          </a>
        </div>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="#navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="navbar-collapse brown collapse mx-2" id="navbarSupportedContent">
          <ul class="navbar-nav">
            <li class="nav-item">
              <RouterLink class="nav-link" :to="{ name: 'home' }">홈</RouterLink> 
            </li>
            <li class="nav-item ">
              <RouterLink class="nav-link" :to="{ name: 'products'}">금융상품정보</RouterLink>
            </li>
            <li class="nav-item ">
              <RouterLink class="nav-link" :to="{ name: 'exchangeRate' }">환율 계산기</RouterLink> 
            </li>
            <li class="nav-item ">
              <RouterLink class="nav-link" :to="{ name: 'bankMap' }">은행 찾기</RouterLink>
            </li>
            <li class="nav-item ">
              <RouterLink class="nav-link" :to="{ name: 'articles' }">게시판</RouterLink>
            </li>   
          </ul>
        </div>
        <div>
          <div :class="{ checkLogin : store.isLogin }" class="m-3">
            <div class="d-flex">
              <RouterLink class="nav-link" :to="{ name: 'login' }">로그인</RouterLink>
              <RouterLink class="nav-link" :to="{ name: 'signUp' }" >회원 가입</RouterLink>
            </div>
          </div>
          <div :class="{ checkLogin : !store.isLogin }" class="m-3">
            <p class="m-0">{{ store.userName }} 님 반갑습니다!</p>
            <div class="d-flex m-0">
              <RouterLink class="nav-link" :to="{ name: 'profile' }" >프로필</RouterLink>
              <a  class="nav-link" @click="store.logOut">로그아웃</a>
            </div>
          </div>
        </div>
      </div>
    </nav>
  </header>
  <div class="viewSpace basicWhite">
    <RouterView />
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useUserStore } from '@/stores/user'
const store = useUserStore()

</script>

<style scoped>
.logbox {
  min-width: 200px;
}
.checkLogin {
  display: none;
}
nav {
  height: 70px;
  width: 100%;
}
ul {
  width: 100%;
}
a, p {
  text-decoration: none;
  margin: 5px;
  color: #F6F1EE;
  font-weight: 700;
  font-size: 1.2rem;
}

</style>

<style>
body, html {
  width: 100%;
  height: 100%;
}
#app {
  width: 100%;
  height: 100%;
}
.viewSpace {
  width: 100%;
  height: calc(100% - 70px);
  display: flex;
  justify-content: center;
  overflow-wrap: normal;
}
/* F6F1EE */

.basicWhite {
  background-color: #F6F1EE !important;
}

.congobrown {
  background-color: #4F4A45 !important;
}
.brown {
  background-color: #6C5F5B !important;
}

.ivory {
  background-color: #B3A492 !important;
}
.orange {
  background-color: #FFA33C !important;
}
.neworange{
  background-color: #ffd19c !important;
}

.font-basicWhite {
  color: #F6F1EE !important;
}

.font-congobrown {
  color: #4F4A45 !important;
  
}

.font-brown {
  color: #6C5F5B !important;
}

.font-orange {
  color: #FFA33C !important;
}

.border-brown {
  border: 1px solid #6C5F5B !important;
}

.shadow-orange{
  box-shadow: 1px 1px 5px #FFA33C !important;
}

*{
  font-family: 'Noto Sans KR', sans-serif;
  font-weight: 400;
}

.han-sans{
  font-family: 'Black Han Sans', sans-serif;
  font-size: 50px;
}

::-webkit-scrollbar {
  display: none;
}
</style>