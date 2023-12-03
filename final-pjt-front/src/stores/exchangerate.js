import { ref } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useExchangeRateStore = defineStore('exchangeRate', () => {
  const countries = ref([])
  const API_URL = import.meta.env.VITE_API_URL

  const getCountries = function() {
    axios({
        method: 'GET',
        url: `${API_URL}/exchange_rate/`
    })
    .then((res) => {
      countries.value = res.data
      console.log(countries)
    })
    .catch((err) => {
        console.log(err)
    })
  }

  return { countries, getCountries }
}, { persist: true })
