<template>
    <div class="d-flex felx-direction-column">    
        <div v-for="option in dataOption">
            <hr>
            <p>{{ option.save_trm }} 개월 옵션</p>
            <p>{{ option.intr_rate_type_nm }}</p>
            <p>{{ option.intr_rate }} %</p>
            <p>{{ option.intr_rate2 }} %</p>
        </div>
    </div>
</template>

<script setup>
const optData = defineProps({
    dataOption: Object
})
</script>

<style scoped>

</style>