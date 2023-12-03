<template>
    <Bar :data="chartInfo"
    :options="chartOptions"/>
</template>

<script setup>
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'
import { Bar } from 'vue-chartjs'
import { useProductStore } from '@/stores/product'
import { computed } from 'vue';
import { storeToRefs } from 'pinia';
ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

const prodStore = useProductStore()
const { chartInfo, userProd, userOpt  } = storeToRefs(prodStore)
const chartOptions= {
    responsive: true,
    maintainAspectRatio: false,
    }
</script>

<style scoped>

</style>