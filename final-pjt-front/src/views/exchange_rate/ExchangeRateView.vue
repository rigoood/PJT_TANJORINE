<template>
<div class="container">
    <div class="row g-2">
    <div class="content-box">

    <div class="select-countries box col-12 row g-2">
        <div class="select-country box col-md-lg-6">
            <select v-model="country1" class="select-box form-select" aria-label="Large select example">
                <option value="" selected>선택1</option>
                <option v-for="country1 in store.countries" :key="country1.cur_unit" :value="country1">
                    {{ country1.cur_nm.split(' ')[0] }}({{ country1.cur_unit }})
                </option>
            </select>
            <div class="country-box">
                <div class="input-group">
                    <input @change="changeCost1" @input="changeCost1" 
                    type="text" class="form-control" v-model.number="inputCost1">
                    <span class="input-group-text">.00</span>
                </div>
                <div v-if="country1" class="result-cost">
                    <div v-if="country1 === country2">
                        {{ inputCost1 }} {{ currencyUnit1(country1.cur_nm) }}
                    </div>
                    <div v-else>
                        {{ Math.round(inputCost1 * 100) / 100 }} {{ currencyUnit1(country1.cur_nm) }}
                    </div>
                </div> <!-- "result-cost" -->
                <div v-else class="result-cost">0</div>
            
            </div> <!-- country-box -->
        </div> <!-- "select-country" -->
        <div class="select-country box col-md-lg-6">
            <select v-model="country2" class="select-box form-select" aria-label="Large select example">
                <option value="" selected>선택2</option>
                <option v-for="country2 in store.countries" :key="country2.cur_unit" :value="country2">
                        {{ country2.cur_nm.split(' ')[0] }}({{ country2.cur_unit }})
                </option>
            </select>
            <div class="country-box">
                <div class="input-group">
                    <input @change="changeCost2" @input="changeCost2" 
                    type="text" class="form-control" v-model.number="inputCost2">
                    <span class="input-group-text">.00</span>
                </div>
                <div v-if="country2" class="result-cost">
                    <div v-if="country1 === country2">
                        {{ inputCost1 }} {{ currencyUnit2(country2.cur_nm) }}
                    </div>
                    <div v-else>
                        {{ Math.round(inputCost2 * 100) / 100 }} {{ currencyUnit2(country2.cur_nm) }}
                    </div>
                </div> <!-- "result-cost" -->
                <div v-else class="result-cost">0</div>
            </div>  <!-- country-box -->
        </div> <!-- "select-country" --> 
    </div> <!-- "select-countryies" -->
    <p class="box col-12" id="explanation">* 엔화, 인도네시아 루피아는 100 단위, 나머지는 모두 1 단위</p>
</div> <!-- "content-box" -->
</div>
</div> <!-- "container" -->
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue'
import { useExchangeRateStore } from '@/stores/exchangeRate'

const store = useExchangeRateStore()
const country1 = ref('')
const country2 = ref('')
const inputCost1 = ref(0)
const inputCost2 = ref(0)


// 국가2 입력금액 변경
const changeCost1 = function() {
    if ((country1.value.cur_unit.includes('(') === false) && country2.value.cur_unit.includes('(') === true ) {  // 국가1 not in [일본, 인도네시아], 국가2 in [일본,인도네시아}
        inputCost2.value = inputCost1.value*country1.value.deal_bas_r.replace(',', '')/country2.value.deal_bas_r.replace(',', '')*100
    } else {
        inputCost2.value = inputCost1.value*country1.value.deal_bas_r.replace(',', '')/country2.value.deal_bas_r.replace(',', '')
    }
    inputCost2.value = Math.round(inputCost2.value * 100) / 100
}


// 국가1 입력금액 변경
const changeCost2 = function() {
    if ((country2.value.cur_unit.includes('(') === false) && country1.value.cur_unit.includes('(') === true ) {  // 국가2 not in [일본, 인도네시아], 국가1 in [일본,인도네시아}
        inputCost1.value = inputCost1.value*country2.value.deal_bas_r.replace(',', '')/country1.value.deal_bas_r.replace(',', '')*100
    } else {
        inputCost1.value = inputCost1.value*country2.value.deal_bas_r.replace(',', '')/country1.value.deal_bas_r.replace(',', '')
    }
    // 국가1 = 국가2 -> 국가1의 inputCost1 출력되도록 & inputCost2 값 변경되면 inputCost1 변경
    if ((country1.value === country2.value) && (inputCost1.value !== inputCost2.value)) {
        inputCost1.value = inputCost2.value
    }
    inputCost1.value = Math.round(inputCost1.value * 100) / 100
}


// 통화단위 처리 (유로, 위안화)
const currencyUnit1 = computed(() => (cur_nm) => {
    return cur_nm.split(' ')[1]?cur_nm.split(' ')[1]:cur_nm
})

const currencyUnit2 = computed(() => (cur_nm) => {
    return cur_nm.split(' ')[1]?cur_nm.split(' ')[1]:cur_nm
})


// 초기화면(국가, 금액 설정 x)에서 국가 두개 선택시 [국가1, 금액:1], [국가2, 금액:계산된금액] 뜨도록
watch([country1, country2], ([newCountry1, newCountry2]) => {
    if (country1.value !== null && country2.value !== null && inputCost1.value === 0 && inputCost2.value === 0) {
        inputCost1.value = 1
        changeCost1()
    }
})


// 국가1 변경 -> 국가2 금액 변경
watch(country1, (newCountry1) => {
    if (country1.value !== null && country2.value !== null && inputCost1.value !== 0) {
        changeCost1()
    }
})


// 국가2 변경 -> 국가2 금액 변경
watch(country2, (newCountry1) => {
    if (country1.value !== null && country2.value !== null && inputCost1.value !== 0) {
        changeCost1()
    }
})


onMounted(() => {
    store.getCountries()
})
</script>

<style scoped>
.content-box {
    display: flex;
    flex-direction: column;
    margin-top: 50px;
}
.select-countries {
    display: flex;
    /* position: relative; */
    justify-content: center;
}
.select-country{
    position: relative;
    display: flex;
    /* justify-content: space-around; */
    justify-content: space-evenly;
    border: 1px solid rgb(185, 185, 185);
    border-radius: 5px;
    margin: 10px;
    padding: 10px;
    width: 450px;
    height: 85px;
    align-items: center;
}
#explanation{
    display: flex;
    justify-content: center
    /* position: absolute; */
}
.select-box{
    width: 185px;
    height: 60px;
    margin: 5px;
}
.result-cost{
    display: flex;
    justify-content: flex-end;
}
</style>