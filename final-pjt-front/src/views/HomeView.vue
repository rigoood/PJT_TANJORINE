<template>
    <div id="carousel" class="carousel slide carousel-fade" data-bs-ride="carousel">
        <div class="carousel-inner">
            <div class="neworange carousel-item active d-flex align-items-center justify-content-evenly" @click.prevent="router.push({ name: 'products'})">
                <div class="d-flex flex-column align-items-center">
                    <img src="../assets/profits.png" width="450" alt="" class="m-3">
                    <h2>"아아...이건 <span class="han-sans">[예금]</span> 이라는거다.."</h2>
                    <h4>"원금과 연 이자율을 보장해주지..."</h4>
                </div>
                <div class="d-flex flex-column align-items-center">
                    <img src="../assets/piggy-bank.png" width="450" alt="" class="m-3">
                    <h4>"조금씩 모아서 크게 돌려받고 싶나..?"</h4>
                    <h2>"그럼 <span class="han-sans">[적금]</span>으로 가라.."</h2>
                </div>
            </div>
            <div class="ivory carousel-item item-box d-flex align-items-center justify-content-evenly" @click.prevent="router.push({ name: 'exchangeRate' })">
                <div class="d-flex flex-column align-items-center">
                    <img src="../assets/forex.png" width="450" alt="" class="m-3">
                    <h2>돈으로 돈을 사도</h2>
                    <h4><span class="han-sans">'저렴'</span>할 때 사야지..</h4>
                </div>
            </div>
            <div class="congobrown carousel-item item-box d-flex align-items-center justify-content-evenly" @click.prevent="router.push({ name: 'bankMap' })">
                <div class="d-flex flex-column align-items-center">
                    <img src="../assets/bank.png" width="450" alt="" class="m-3">
                    <h2 class="text-info han-sans">원하는 은행</h2>
                    <h4 class="text-info">어디에 있는지 알고 가자.</h4>
                </div>
            </div>
        </div>
        <button class="carousel-control-prev" type="button" data-bs-target="#carousel" data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#carousel" data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
        </button>
    </div>
</template>

<script setup>
import { useRouter } from 'vue-router';

const router = useRouter()
</script>

<style scoped>
.carousel {
    height: 100%;
    width: 100%;
}
.carousel-inner {
    height: 100%;
}
.carousel-item {
    height: 100%;
}
</style>