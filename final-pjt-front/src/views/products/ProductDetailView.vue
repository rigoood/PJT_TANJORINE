<template>
    <div class="box">
        <div class="main ivory border border-warning border-3 m-3 p-3">
            <ProductDetail :data-prod="product"/>
            <vue-good-table
                :columns="typeCol"
                :rows="rows"
                @row-click="onRowClick"
                />
        </div>
    </div>
</template>

<script setup>
import axios from 'axios';
import { ref, onMounted, computed } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { VueGoodTable } from 'vue-good-table-next';
import { useUserStore } from '@/stores/user'
import ProductDetail from '@/components/products/ProductDetail.vue'
import 'vue-good-table-next/dist/vue-good-table-next.css'
const user = useUserStore()
const route = useRoute()
const router = useRouter()
const product = ref({})
const options = ref({})
const rows = ref([])
const selectOpt = ref('')
onMounted(() => {
    axios({
        method:'get',
        url: `http://127.0.0.1:8000/products/detail/${route.params.type}/${route.params.id}/`,
    })
    .then((res) => {
        product.value = res.data.product
        options.value = res.data.options
        console.log(route.params.type)
        makeRows(options.value)
    })
})

const columns1 = [
        { label: '예치 기간', field: 'save_trm',},
        { label: '이자 방식', field: 'intr_rate_type_nm',},
        { label: '기본 금리', field: 'intr_rate',},
        { label: '최대 금리', field: 'intr_rate2',},
      ]

const columns2 = [
        { label: '예치 기간', field: 'save_trm',},
        { label: '적금 방식', field: 'rsrv_type_nm',},
        { label: '이자 방식', field: 'intr_rate_type_nm',},
        { label: '기본 금리', field: 'intr_rate',},
        { label: '최대 금리', field: 'intr_rate2',},
      ]
      
const typeCol = computed(() => {
    if (route.params.type === 'D') return columns1
    else return columns2
})

const makeRows = function (opts) {
    for(const k in opts) {
        let row_data = {
            id: null,
            save_trm: null,
            rsrv_type_nm: null,
            intr_rate_type_nm: null,
            intr_rate: null,
            intr_rate2: null,
        }
        row_data.id = opts[k].id
        row_data.save_trm = opts[k].save_trm
        row_data.rsrv_type_nm = opts[k].rsrv_type_nm
        row_data.intr_rate_type_nm = opts[k].intr_rate_type_nm
        row_data.intr_rate = opts[k].intr_rate
        row_data.intr_rate2 = opts[k].intr_rate2
        rows.value.push(row_data)
    }
}

const onRowClick = function(params) {
    const row = params.row
    const check = confirm(`${row.save_trm}개월 예치기간 옵션을 선택 하시겠습니까? \n ${row.intr_rate}% 기본 금리 / ${row.intr_rate2}% 최대 금리`)
    if (check) {
        const data = {
            user: user.userEmail,
            code: `${route.params.type}/$${product.value.fin_co_no}/$${product.value.fin_prdt_cd}/$`,
            cpt_cd: row.id
        }
        console.log(data)
        axios({
            method:'post',
            url: 'http://127.0.0.1:8000/products/signUpProd/',
            data: data,
        })
        .then((res) => {
            if (res.data.result === 'Done') {
                alert('가입되었습니다!')
            } else if (res.data.result === 'Already') {
                alert('이미 가입한 상품입니다.')
            }
        })
    } else {
        return
    }
}
</script>

<style scoped>
.box {
    width: 100%;
    display: flex;
    justify-content: center;
}
.main {
    width: 80%;
}
</style>