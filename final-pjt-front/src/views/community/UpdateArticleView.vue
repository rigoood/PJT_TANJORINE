<template>
  <div class="container">
    <form @submit.prevent="updateArticle">
      <div>
        <label for="edit=category"></label>
        <select class="form-select form-select-sm" id="edit-category" v-model="newCate">
          <option value="" selected>카테고리 선택</option>
          <option v-for="category in store.categories" :value="category">
            <p>{{ category.name }}</p>
          </option>
        </select>
      </div>
        <div>
            <label for="title" class="font-brown" style="font-size:17px; font-weight: 500;">제목</label>
            <input class="form-control" type="text" id="title" v-model.trim="articleTitle">
        </div>
        <div>
            <label for="content" class="font-brown" style="font-size:17px; font-weight: 500;">내용</label>
            <textarea class="form-control" id="content" v-model="articleContent"></textarea>
        </div>      
        <div id="edit-button">
        <input class="btn btn-dark brown border-brown" style="color:white;" type="submit" value="수정">
        </div>
    </form>
  </div>
</template>

<script setup>
import axios from 'axios';
import { useRoute, useRouter } from 'vue-router';
import { useCommunityStore } from '@/stores/community';
import { useUserStore } from '@/stores/user'
import { ref, onMounted } from 'vue';

const userStore = useUserStore()
const route = useRoute()
const router = useRouter()
const store = useCommunityStore()

const article = ref(null)
const articleTitle = ref(null)
const articleContent = ref(null)
const loginUser = ref(null)
const newCate = ref('')

const updateArticle = function() {
  if (article.value.user.email === loginUser.value && loginUser.value !== null) {
    axios({
      method: 'PUT',
      url: `${store.API_URL}/community/articles/${route.params.id}/`,
      headers: {
          Authorization: `Token ${userStore.token}`
      },
      data: {
        category: newCate.value.pk,
        title: title.value,
        content: content.value,
      },
    })
    .then((res) => {
      console.log(res)
      router.push({ name: 'articles' })
    })
    .catch((err) => {
      console.log(err)
    })
  } else {
    alert('수정할 수 없습니다.')
  }
}

onMounted(() => {
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
  })
  .catch((err) => {
    console.log(err)
  })

  axios({
    method: 'GET',
    url: `${store.API_URL}/community/articles/${route.params.id}/`
  })
  .then((res) => {
    article.value = res.data
  
    articleTitle.value = res.data.title
    articleContent.value = res.data.content
    // console.log(article.value)
  })
  .catch((err) => {
    console.log(err)
  })


  // console.log(loginUser.value)
})

// console.log(loginUser)
</script>

<style scoped>
#edit-category{
  margin: 5px;
  width: 200px;
}
#title{
  margin: 5px;
  width: 100%;
}
#content{
  margin: 5px;
  width: 100%;
  height: 300px;
}
label{
  margin: 5px;
}
#edit-button{
  display: flex;
  justify-content: end;
}
</style>

