<template>
  <div>
    <hr>
    <CommentListItem 
      v-for="comment in store.comments"
      :key="comment.id"
      :value="comment.article.pk"
      :comment="comment"
      />
  </div>
</template>

<script setup>
import { useCommunityStore } from '@/stores/community';
import CommentListItem from '@/components/CommentListItem.vue'
import { onMounted } from 'vue';

const store = useCommunityStore()

onMounted(() => {
  store.getComments()
})
</script>
