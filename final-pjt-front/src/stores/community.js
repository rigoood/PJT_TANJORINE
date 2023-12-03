import { ref } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useCommunityStore = defineStore('community', () => {
  const API_URL = import.meta.env.VITE_API_URL
  const articles = ref([])
  const comments = ref([])
  const categories = ref([])

  const getCategories = function() {
    axios({
      method: 'GET',
      url: `${API_URL}/community/category/`
    })
    .then((res) => {
      categories.value = res.data
    })
    .catch((err) => {
      console.log(err)
    })
  }

  const getArticles = function() {
    axios({
      method: 'GET',
      url: `${API_URL}/community/articles/`,
    })
    .then((res) => {
      articles.value = res.data
      console.log(articles)
    })
    .catch((err) => {
      console.log(err)
    })
  }
  
  const getComments = function() {
    axios({
      method: 'GET',
      url: `${API_URL}/community/comments/`
    })
    .then((res) => {
      // console.log(res)
      comments.value = res.data
    })
    .catch((err) => {
      console.log(err)
    })
  }
  return { API_URL, articles, getArticles, comments, getComments, categories, getCategories }
})