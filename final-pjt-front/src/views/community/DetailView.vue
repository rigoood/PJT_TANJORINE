<template>
  <div class="container">
    <div v-if="article">
    <div id="button-box">
      <RouterLink class="custom-btn btn" :to="{ name: 'articles' }">목록</RouterLink>
      <!-- article.value.user.email => 변수 만들어 쓰니까 새로고침 해야 뜸 -->
      <div v-if="article.user.email === loginUser && loginUser !== null">
        <RouterLink :to="{ name: 'update', params: {id: article.id} }">
          <button class="custom-btn btn" style="margin-right: 3px;">수정</button>
        </RouterLink>
        <button class="custom-btn btn" @click="deleteArticle">삭제</button>
      </div>
    </div>

      <div style="margin: 30px 0px 20px;">
        <div class="font-brown" style="font-size: 12px;">카테고리</div>
        <div class="font-brown" style="font-weight: 500;">{{ article.category.name }}</div>
      </div>
      <div id="title">{{ article.title }}</div>
      <hr class="brown" style="height: 5px;">
      <div id="user-and-date">
        <div style="margin-right: 15px;">🙍‍♂️ {{ article.user.username }}</div>
        <div>🕘 {{ article.created_at.slice(0, 10) + " (" + article.created_at.slice(11,19) + ")"}}</div>
      </div>
      <div id="article-content">{{ article.content }}</div>
    

      <div id="comment-box">
        <div style="display: flex; align-items: flex-end; font-size: 19px; font-weight: 500;">댓글 <div style="font-size: 14px;"> ({{ article.comment_count }})</div></div>
        <br>
        <div v-if="loginUser">
          <form @submit.prevent="createComment">
            <div id="write-comment">
              <label for="content"></label>
              <textarea class="form-control" placeholder="댓글을 입력해주세요." v-model.trim="content" id="content"></textarea>
              <input class="btn btn-dark brown border-brown" style="color:white; margin-left: 5px;" type="submit" value="등록">
            </div>
          </form>
        </div>
        <div v-else>
          <p>로그인 후 이용해주세요.</p>
        </div>
        <CommentList/>
      </div>
    </div>
  </div> <!-- "container" -->
</template>

<script setup>
import axios from 'axios';
import { ref, onMounted } from 'vue';
import { useCommunityStore } from '@/stores/community';
import { useUserStore } from '@/stores/user'
import { useRouter, useRoute } from 'vue-router';
import CommentList from '@/components/CommentList.vue';


const userStore = useUserStore()
const store = useCommunityStore()
const route = useRoute()
const router = useRouter()
const article = ref(null)
const content = ref(null)

const loginUser = ref(null)

const deleteArticle = function() {
  // console.log(article.value.user.email)
  if (article.value.user.email === loginUser.value && loginUser.value !== null) {
    axios({
      method: 'DELETE',
      url: `${store.API_URL}/community/articles/${route.params.id}/`
    })
    .then(() => {
      router.push({ name: 'articles'})
    })
    .catch((err) => {
      console.log(err)
    })
  } else {
    alert('삭제할 수 없습니다.')
  }
}

const createComment = function() {
  axios({
    method: 'POST',
    url: `${store.API_URL}/community/articles/${route.params.id}/comments/`,
    headers: {
        Authorization: `Token ${userStore.token}`
    },
    data: {
      content: content.value,
    },
  })
  .then(() => {
    router.go()
    console.log(comment)
  })
  .catch((err) => {
    console.log(err)
  })
}


onMounted(() => {
  axios({
    method: 'GET',
    url: `${store.API_URL}/community/articles/${route.params.id}/`
  })
  .then((res) => {
    article.value = res.data
    console.log(article.value)
  })
  .catch((err) => {
    console.log(err)
  })

  axios({
    method: 'GET',
    url: `${store.API_URL}/accounts/user/`,
    headers: {
      Authorization: `Token ${userStore.token}`
    }
  })
  .then((res) => {
    loginUser.value = res.data.email
    console.log(loginUser)
  })
  .catch((err) => {
    console.log(err)
  })
})
</script>

<style scoped>
#button-box{
  margin-top: 10px;
  display: flex;
  justify-content: space-between;
}
.custom-btn{
  margin: 10px 0px;
  font-size: 13px;
  border-radius:5px;
  background-color: white;

  text-decoration: none;
  color: black;
}
#title{
  font-size: 30px;
  font-weight: 800;
  text-decoration: none;
  color: black;
}
#user-and-date{
  display: flex;
  margin-bottom: 20px;
}
#article-content{
  border-radius: 8px;
  /* margin: 20px 0px; */
  background-color: white;
  padding: 15px;
  font-size: 16px;
  margin: 5px 2px;
  height: 300px;
  overflow-y: scroll;
}
#comment-box{
  /* border-radius: 8px; */
  margin: 20px 0px;
  padding: 15px;
}
#write-comment{
  display: flex;
  justify-content: end;
}
</style>
