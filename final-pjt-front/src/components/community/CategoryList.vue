<template>
  <div class="row">
    <CategoryListItem class="cate box col-6"
      v-for="category in store.categories"
      :key="category.id"
      :category="category"
    />
  </div>
</template>

<script setup>
import { useCommunityStore } from '@/stores/community';
import CategoryListItem from './CategoryListItem.vue';
import { onMounted } from 'vue';

const store = useCommunityStore()

onMounted(() => {
  store.getCategories()
})
</script>

<style scoped>
.cate{
  margin: 15px 0px;
}
</style>