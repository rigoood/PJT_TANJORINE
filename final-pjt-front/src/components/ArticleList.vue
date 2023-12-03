<template>
  <div>
    <div v-for="article in store.articles">
      <div v-if="cate === '전체'">
      <div v-if="article">
        <div id="num-and-cate">
          <div class="article-num font-brown">No. {{ article.id }}</div>
          <div class="article-num font-brown">{{ article.category.name }}</div>
        </div>
        <RouterLink class="title font-congobrown" :to="{ name: 'detail', params: { id: article.id } }">
          {{ article.title }}
        </RouterLink>
        <p class="content">{{ article.content.length>20?article.content.slice(0, 20) + '...':article.content }}</p>
        <p class="date-and-author font-brown">작성일 : {{ article.created_at.slice(0, 10) }} | 작성자 : {{ article.user.username }}</p>
        <hr>
      </div>
      <div v-else>
        작성된 게시글이 없습니다.
      </div>
    </div>  

    <div v-else-if="cate.name === article.category.name">
      <div id="num-and-cate">
        <div class="article-num font-brown">No. {{ article.id }}</div>
        <div class="article-num font-brown">{{ article.category.name }}</div>
      </div>
      <RouterLink class="title font-congobrown" :to="{ name: 'detail', params: { id: article.id } }">
        {{ article.title }}
      </RouterLink>
      <p class="content">{{ article.content.length>20?article.content.slice(0, 20) + '...':article.content }}</p>
      <p class="date-and-author font-brown">작성일 : {{ article.created_at.slice(0, 10) }} | 작성자 : {{ article.user.username }}</p>
      <hr>
    </div>
    <!-- <div v-else>
      <div v-if="!Object.values(store.articles).filter((item) => item.category.name === cate.name).length">
        작성된 게시글이 없습니다.
      </div>
    </div> -->
  </div>
  </div>
</template>

<script setup>
import { useCommunityStore } from '@/stores/community';
import { onMounted } from 'vue';

const store = useCommunityStore()

defineProps({
  cate: Object,
})

onMounted(() => {
  store.getCategories()
})
</script>

<style scoped>
#num-and-cate{
  display: flex;
  justify-content: space-between;
}
.article-num{
  font-size: 12.5px;
  color: gray;
  margin: 10px 0px;
}
.title{
  font-size: 21px;
  font-weight: 800;
  text-decoration: none;
  color: black;
}
.content{
  font-size: 15px;
  margin: 5px 2px;
}
.date-and-author{
  text-align: end;
  font-size: 13.5px;
  color: gray;
  margin: 0px;
}

</style>