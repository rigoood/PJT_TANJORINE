<template>
  <div class="container">
    <form @submit.prevent="createArticle">
      <div>
        <label for="category"></label>
          <select class="form-select form-select-sm" aria-label="Small select example" v-model="category" name="category" id="category">
            <option value="" selected>카테고리 선택</option>
            <option v-for="category in store.categories" :value="category">
              <p>{{ category.name }}</p>
            </option>
          </select>
        
      </div>
      <div>
        <label for="title" class="font-brown" style="font-size:17px; font-weight: 500;">제목</label>
        <input class="form-control" type="text" v-model.trim="title" id="title">
      </div>
      <div>
        <label for="content" class="font-brown" style="font-size:17px; font-weight: 500;">내용</label>
        <textarea class="form-control" v-model.trim="content" id="content"></textarea>
      </div>
      <div id="post-button">
        <input class="btn btn-dark brown border-brown" style="color:white;" type="submit" value="등록">
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { useCommunityStore } from '@/stores/community';
import { useUserStore } from '@/stores/user'
import { useRouter } from 'vue-router';

const title = ref(null)
const content = ref(null)
const store = useCommunityStore()
const userStore = useUserStore()
const router = useRouter()
const category = ref('')

console.log(userStore.token)

const createArticle = function() {
  const data= {
      // category: {'pk': category.value.pk, 'name': category.value.name},
      category: category.value.pk,
      title: title.value,
      content: content.value,
    }
  console.log(data)
  axios({
    method: 'POST',
    url: `${store.API_URL}/community/articles/`,
    headers: {
        Authorization: `Token ${userStore.token}`
    },
    data: {
      // category: {'pk': category.value.pk, 'name': category.value.name},
      category: category.value.pk,
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
}

onMounted(() => {
  store.getCategories()
})

</script>

<style scoped>
#category{
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
#post-button{
  display: flex;
  justify-content: end;
}
</style>
