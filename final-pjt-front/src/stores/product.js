import { ref, computed, onMounted, watch } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
export const useProductStore = defineStore('product', () => {
    const userProd = ref({})
    const userOpt = ref({})
    const chartInfo = ref({
        labels:[],
        datasets:[
            {
                label: '기본 금리',
                data: [],
                backgroundColor: [
                    'rgba(255, 99, 132, 0.7)',
                    ],
                borderColor: [
                    'rgb(75, 192, 192)',
                    ],
            },
            {
                label: '최대 금리',
                data: [],
                backgroundColor: [
                    'rgba(100, 199, 132, 0.7)',
                    ],
                borderColor: [
                    'rgb(75, 192, 192)',
                    ],
            }
        ],
    })
    const signedProductsInfo = function(data) {
        axios({
                method:'post',
                url: `http://127.0.0.1:8000/products/signedProd/`,
                data: data
            })
            .then((res) => {
                userProd.value=res.data.products
                userOpt.value=res.data.options
                makeChart(userProd.value, userOpt.value)
            })
            .catch((err) => {
                console.log(err)
            })
    }
    const makeChart = function(prods, opts) {
        let labels = []
        let datasets = [
            {
                label: '기본 금리',
                data: [],
                backgroundColor: [
                    'rgba(255, 99, 132, 0.7)',
                    ],
                borderColor: [
                    'rgb(75, 192, 192)',
                    ],
            },
            {
                label: '최대 금리',
                data: [],
                backgroundColor: [
                    'rgba(100, 199, 132, 0.7)',
                    ],
                borderColor: [
                    'rgb(75, 192, 192)',
                    ],
            }
        ]
        for (const prod in prods) {
            labels.push(prods[prod][0].fin_prdt_nm)
            datasets[0].data.push(opts[prod].intr_rate)
            datasets[1].data.push(opts[prod].intr_rate2)
        }
        chartInfo.value={
            labels:labels,
            datasets:datasets,
        }
    }
    return { signedProductsInfo, userProd, userOpt, chartInfo}
})
