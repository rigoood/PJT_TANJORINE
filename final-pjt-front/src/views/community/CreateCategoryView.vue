<template>
<div class="container">
    <h2 class="page-title">카테고리 관리</h2>
    <div v-if="isStaff">
        <div id="category-box">
            <form @submit.prevent="createCategory">
                <label class="cate-page-title" for="create-category">카테고리 생성</label>
                <br>
                <div class="input-group mb-3" id="input-box">
                    <input type="text" class="form-control" placeholder="카테고리 이름" name="create-category" id="create-category" v-model.trim="name" aria-describedby="button-addon2">
                    <button class="btn btn-outline-secondary" type="submit" id="button-addon2">생성</button>
                </div>
            </form>
            <br>
            <p class="cate-page-title">카테고리 목록</p>
            <CategoryList/>
        </div>
        <div>
        </div>
    </div>
    <div v-else>
        <h2>관리자 전용 페이지 입니다.</h2>
    </div>
</div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { useCommunityStore } from '@/stores/community';
import { useUserStore } from '@/stores/user'
import { useRouter } from 'vue-router';
import CategoryList from '../../components/community/CategoryList.vue';

const name = ref(null)
const store = useCommunityStore()
const userStore = useUserStore()
const router = useRouter()
const isStaff = ref(false)
const mainCate = ref(false)

// console.log(isStaff.value)
const createCategory = function() {
    if (isStaff.value) {
        axios({
            method: 'POST',
            url: `${store.API_URL}/community/category/`,
            data: {
                name: name.value,
                main_category: mainCate.value
            }
        })
        .then((res) => {
            router.go()
        console.log(res)
        })
        .catch((err) => {
            console.log(err)
        })
    } else {
        alert('카테고리를 생성할 수 없습니다.')
    }
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
    isStaff.value = res.data.is_staff
  })
  .catch((err) => {
    console.log(err)
  })
})
</script>

<style scoped>
#input-box{
    margin: 7px 0px;
    width: 450px;
}
#category-box{
    padding: 7px;
    display: flex;
    flex-direction: column;
}
.cate-page-title{
    margin-top: 10px;
    font-weight: 600;
    font-size: 20px;
}

</style>