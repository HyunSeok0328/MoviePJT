<template>
  <div>
    <h4>어서오세요, {{ user.username }}님!</h4>
    <p class="my-4">{{ user.username }}님을 위한 추천 영화 리스트입니다 </p>
    
    <recommend></recommend>
  </div>
</template>

// <script>
import axios from 'axios';
import Recommend from '@/components/profile/Recommend'

export default {
  name: 'Profile',
  data: function(){
    return{
      reviews: [],
      user: [],
      comments: [],
    }
  },
  components: {
    Recommend,
  },
  created: function(){
    this.getUser()
    this.getReviews()
    this.getComments()
  },
  methods: {
      setToken: function(){
        const token = localStorage.getItem('jwt')
        const config = {
          Authorization: `JWT ${token}`
        }
        return config
      },
      getReviews: function () {
        axios({
          method: 'get',
          url: 'http://127.0.0.1:8000/community/review/',
          headers: this.setToken()
        })
          .then(res => {
            this.reviews = res.data
          })
          .catch(err => {
            console.log(err)
          })
      },
      getComments: function () {
        axios({
          method: 'get',
          url: `http://127.0.0.1:8000/community/review/commentlist/`,
          headers: this.setToken()
        })
          .then(res => {
            this.comments = res.data
          })
          .catch(err => {
            console.log(err)
          })
      },
      getUser: function(){
        axios({
          method: 'get',
          url: `http://127.0.0.1:8000/accounts/username/`,
          headers: this.setToken()
        })
          .then((res) => {
            this.user = res.data
          })
          .catch(err => {
            console.log(err)
          })
      },
  },

}
</script>

<style>

</style>