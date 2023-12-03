<template>
    <div class="main">
        <div class="btnbox">
            <button class="btn types btn-warning m-1" @click="click" :disabled="showtype">
            정기예금
            </button>
            <button class="btn types btn-warning m-1" @click="click" :disabled="!showtype">
            정기적금
            </button>
        </div>
        <div class="tablespace">
            <DepositeTable v-show="showtype"/>
            <SavingTable v-show="!showtype"/>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import DepositeTable from '@/components/products/DepositeTable.vue';
import SavingTable from '@/components/products/SavingTable.vue';
const showtype = ref(true)
const click = function () {
    showtype.value = !showtype.value
}
</script>

<style scoped>
.types {
    border: 1px solid black;
}

.types:hover {
    border: 1px solid black;
    background-color: #f0f0f0;
}
.main {
    width: 90%;
}
.tablespace {
    height: 300px;
}
</style>