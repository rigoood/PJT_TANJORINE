import { ref } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import data from '@/assets/data.json'


export const useBankMapStore = defineStore('bankMap', () => {
    const API_URL = import.meta.env.VITE_API_URL

    const siDo = ref([])
    const siGunGu = ref([])
    const banks = ref([])

    const resetSiGunGu = function() {
        siGunGu.value = []
        banks.value = []
    }

    const getSiDo = function() {
        axios({
            method: 'GET',
            url: `https://grpc-proxy-server-mkvo6j4wsq-du.a.run.app/v1/regcodes?regcode_pattern=*00000000`
        })
        .then((res) => {
            siDo.value = res.data.regcodes
        })
        .catch((err) => {
            console.log(err)
        })
    }

    const getSiGunGu = function(code) {
        axios({
            method: 'GET',
            url: `https://grpc-proxy-server-mkvo6j4wsq-du.a.run.app/v1/regcodes?regcode_pattern=${code}*00000`
        })
        .then((res) => {
            siGunGu.value = []
            const siGunGuData = res.data.regcodes
            for (let data of siGunGuData) {
                const sgg = data.name.split(' ')[1]
                if (!siGunGu.value.includes(sgg) && sgg!==undefined) {
                    siGunGu.value.push(sgg);
                }
            }
        })
        .catch((err) => {
            console.log(err)
        })
    }

    const getBank = function() {
        /* data.json */
        // const bankList = data
        // for (let bk of bankList) {
        //     const bank_nm = bk.fields.kor_co_nm
        //     if (!banks.value.includes(bank_nm) && bank_nm !== undefined) {
        //         banks.value.push(bank_nm);
        //     }
        // }

        /* API KEY */
        axios({
            method: 'GET',
            url: `${API_URL}/maps/bank/`
        })
        .then((res) => {
            const bankList = res.data.result.baseList
            for (let bk of bankList) {
                const bank_nm = bk.kor_co_nm
                if (!banks.value.includes(bank_nm) && bank_nm !== undefined) {
                    banks.value.push(bank_nm);
                }
            }
            console.log(banks.value)
        })
        .catch((err) => {
            console.log(err)
        })
    }

    return { siDo, getSiDo, siGunGu, getSiGunGu, resetSiGunGu, banks, getBank }

}, { persist: true })