<template>
  <div class="container">
    <div id="community-nav">
      <div v-if="isStaff" class="community-nav-item btn">
        <RouterLink class="nav-item-1" :to="{ name: 'createCategory' }">카테고리 관리</RouterLink>
      </div>
      <div v-if="loginUser" class="community-nav-item btn">
        <RouterLink class="nav-item-1" :to="{ name: 'create' }">글 작성</RouterLink>
      </div>
      <select v-model="selectCate" class="community-nav-item" style="border:0px;">
        <option selected>전체</option>
        <option v-for="category in store.categories" :value="category">
          <p>{{ category.name }}</p>
        </option>
      </select>
    </div>
    <hr style="margin: 0 0 1rem;">
    <ArticleList
    :cate = selectCate
    />
  </div>
</template>

<script setup>
import axios from 'axios';
import { ref, onMounted } from 'vue';
import { useCommunityStore } from '@/stores/community';
import { useUserStore } from '@/stores/user'
import { RouterLink } from 'vue-router';
import ArticleList from '@/components/ArticleList.vue';


const store = useCommunityStore()
const userStore = useUserStore()

const loginUser = ref(null)
const isStaff = ref(false)

const selectCate = ref("전체")


onMounted(() => {
  store.getArticles()
  store.getCategories()
  
  axios({
    method: 'GET',
    url: `${store.API_URL}/accounts/user/`,
    headers: {
      Authorization: `Token ${userStore.token}`
    }
  })
  .then((res) => {
    loginUser.value = res.data.email
    isStaff.value = res.data.is_staff
  })
  .catch((err) => {
    console.log(err)
  })
})
</script>

<style scoped>
#community-nav{
  display: flex;
  justify-content: flex-end;
  margin: 10px;
}
.community-nav-item{
  margin: 5px;
  font-size: 13px;
  border-radius:5px;
  background-color: white;
}
.nav-item-1{
  text-decoration: none;
  color: black;
}
</style>
