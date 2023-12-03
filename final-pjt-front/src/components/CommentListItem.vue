<template>
<div v-if="Number(route.params.id) === comment.article.pk">
  <div id="comment-box">
    <div style="margin-right: 15px; width: 15%; font-weight: 600;">🙍‍♂️ {{ comment.user.username }}</div>
    <div v-if="comment.user.email === loginUser && loginUser !== null" style=" width: 85%;">
      <div v-if="showContent">
        <div class="content-box">
          <div>{{ comment.content }}</div>
          <div v-if="comment.created_at !== comment.updated_at" style="font-size: 11.5px;">(수정됨)</div>
          <button class="custom-btn btn btn-light brown" style="color:white; margin-left: 10px;" @click="clickUpdate">수정</button>
          <button class="custom-btn btn border-brown" @click="deleteComment(comment.id)">삭제</button>
        </div>
      </div>
      <div v-else>
        <form @submit.prevent="updateComment(comment.id)">
          <div>
            <textarea class="form-control" v-model.trim="content" id="content"></textarea>
          </div>
          <div id="edit-button">
            <input class="custom-btn btn btn-light brown" style="color:white;" type="submit" value="수정">
          </div>
        </form>
      </div>
    </div>
    <div v-else style="width: 85%;">
      <div class="content-box">
        <div>{{ comment.content }}</div>
        <div v-if="comment.created_at !== comment.updated_at" style="font-size: 11.5px;">(수정됨)</div>
      </div>
    </div>
    <hr>
  </div>
</div>

</template>

<script setup>
import { useRouter, useRoute } from 'vue-router';
import { useCommunityStore } from '@/stores/community';
import { useUserStore } from '@/stores/user'
import axios from 'axios';
import { ref, onMounted } from 'vue'


const API_URL = import.meta.env.VITE_API_URL


const route = useRoute()
const router = useRouter()
const store = useCommunityStore()
const userStore = useUserStore()
const showContent = ref(true)
const loginUser = ref(null)

const props = defineProps({
  comment: Object,
})

const comment = ref(props.comment)
const content = ref(comment.value.content)

const updateComment = function(commentId) {
  if (comment.value.user.email === loginUser.value && loginUser.value !== null) {
    axios({
      method: 'PUT',
      url: `${API_URL}/community/comments/${commentId}/`,
      headers: {
        Authorization: `Token ${userStore.token}`
      },
      data: {
        content: content.value,
      },
    })
    .then((res) => {
        console.log(res)
        showContent.value != showContent.value
        router.go()
    })
    .catch((err) => {
      console.log(err)
    })
  } else {
    alert('수정할 수 없습니다.')
  }
}

const deleteComment = function(commentId) {
  if (comment.value.user.email === loginUser.value && loginUser.value !== null) {
    console.log(1)
    axios({
      method: 'DELETE',
      url: `${store.API_URL}/community/comments/${commentId}/`
    })
    .then(() => {
      router.go()
      // alert('댓글이 삭제되었습니다.')
    })
    .catch(() => {
      console.log(err)
    })
  } else {
    alert('삭제할 수 없습니다.')
  }
}

const clickUpdate = function() {
  showContent.value = !showContent.value
}

onMounted(() => {
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
})


</script>

<style scoped>
#comment-box{
  display: flex;
  align-items: flex-start;
}
.content-box{
  display: flex;
  align-items: center;
}
.custom-btn{
  margin: 0px 1px;
  font-size: 12px;
  border-radius:6px;
  padding: 3px 5px;
  text-decoration: none;
  color: black;
}
#edit-button{
  display: flex;
  justify-content: end;
}
</style>